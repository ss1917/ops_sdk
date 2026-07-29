# -*- coding: utf-8 -*-
"""开放 API 客户端：AK/SK 签名请求 CODO 网关。"""

import json
import logging
from typing import Any, Dict, Optional
from urllib.parse import urlencode, urlparse
import requests
from .configs import configs
from .consts import const
from .openapi_sign import build_auth_headers

logger = logging.getLogger(__name__)


class OpenAPIClient:
    def __init__(
        self,
        access_key: str,
        secret_key: str,
        endpoint: str = None,
        request_timeout: int = 10,
    ):
        self.access_key = access_key
        self.secret_key = secret_key
        self.request_timeout = request_timeout
        if endpoint:
            self.endpoint = endpoint.rstrip("/")
        else:
            self.endpoint = (configs.get(const.WEBSITE_API_GW_URL) or "http://gw.opendevops.cn").rstrip(
                "/"
            )

    def _path_and_query(self, url: str, params: Optional[dict]):
        if url.startswith("http://") or url.startswith("https://"):
            parsed = urlparse(url)
            path = parsed.path or "/"
            # merge query from url
            q = {}
            if parsed.query:
                from urllib.parse import parse_qs

                for k, vs in parse_qs(parsed.query, keep_blank_values=True).items():
                    q[k] = vs[0] if len(vs) == 1 else vs
            if params:
                q.update(params)
            return path, q, f"{parsed.scheme}://{parsed.netloc}"
        path = url if url.startswith("/") else "/" + url
        return path, params or {}, self.endpoint

    def request(
        self,
        method: str,
        url: str,
        params: dict = None,
        data: Any = None,
        json_body: Any = None,
        headers: dict = None,
    ) -> requests.Response:
        path, query, base = self._path_and_query(url, params)
        method_u = method.upper()
        body_bytes = None
        content_type = None
        if json_body is not None:
            body_bytes = json.dumps(json_body, ensure_ascii=False, separators=(",", ":")).encode(
                "utf-8"
            )
            content_type = "application/json"
        elif data is not None:
            if isinstance(data, (dict, list)):
                body_bytes = json.dumps(data, ensure_ascii=False, separators=(",", ":")).encode(
                    "utf-8"
                )
                content_type = "application/json"
            elif isinstance(data, str):
                body_bytes = data.encode("utf-8")
            else:
                body_bytes = data

        auth_headers = build_auth_headers(
            self.access_key,
            self.secret_key,
            method_u,
            path,
            query=query,
            body=body_bytes,
            content_type=content_type,
        )
        final_headers = dict(headers or {})
        final_headers.update(auth_headers)

        full_url = f"{base}{path}"
        if query:
            full_url = f"{full_url}?{urlencode(query, doseq=True)}"

        return requests.request(
            method_u,
            full_url,
            headers=final_headers,
            data=body_bytes,
            timeout=self.request_timeout,
        )

    def with_params_data_url(self, **kwargs):
        url = kwargs.get("url")
        method = kwargs.get("method") or "GET"
        params = kwargs.get("params")
        body = kwargs.get("body")
        req_json = kwargs.get("json")
        if method.upper() in ("GET", "DELETE", "HEAD"):
            return dict(method=method, url=url, params=params)
        return dict(method=method, url=url, params=params, body=body, json=req_json)

    def do_action(self, **kwargs) -> str:
        return self.do_action_v2(**kwargs).text

    def do_action_v2(self, **kwargs) -> requests.Response:
        return self.do_action_v3(**kwargs)

    def do_action_v3(self, **kwargs) -> requests.Response:
        method = kwargs.get("method") or "GET"
        url = kwargs.get("url")
        params = kwargs.get("params")
        if kwargs.get("json") is not None:
            return self.request(method, url, params=params, json_body=kwargs.get("json"))
        body = kwargs.get("body")
        return self.request(method, url, params=params, data=body)
