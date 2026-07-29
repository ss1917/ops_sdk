#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""CODO1-HMAC-SHA256 签名（与网关 / Go SDK 对齐）。"""

import hashlib
import hmac
import secrets
import time
from typing import Dict, Mapping, Optional, Union
from urllib.parse import quote


def sha256_hex(data: Union[bytes, str, None]) -> str:
    if data is None:
        data = b""
    if isinstance(data, str):
        data = data.encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def hmac_sha256_hex(key: str, msg: str) -> str:
    return hmac.new(key.encode("utf-8"), msg.encode("utf-8"), hashlib.sha256).hexdigest()


def canonical_query(params: Optional[Mapping] = None) -> str:
    if not params:
        return ""
    items = []
    for k in sorted(params.keys()):
        v = params[k]
        if isinstance(v, (list, tuple)):
            for vv in sorted(str(x) for x in v):
                items.append(f"{quote(str(k), safe='-_.~')}={quote(str(vv), safe='-_.~')}")
        elif v is None:
            continue
        else:
            items.append(f"{quote(str(k), safe='-_.~')}={quote(str(v), safe='-_.~')}")
    return "&".join(items)


def build_canonical_request(
    method: str,
    uri: str,
    query: Optional[Mapping],
    headers: Mapping[str, str],
    body: Union[bytes, str, None],
) -> str:
    if body is None:
        body_b = b""
    elif isinstance(body, str):
        body_b = body.encode("utf-8")
    else:
        body_b = body
    normalized = {str(k).lower(): str(v).strip() for k, v in headers.items()}
    names = sorted(normalized.keys())
    canonical_headers = "".join(f"{n}:{normalized[n]}\n" for n in names)
    signed_headers = ";".join(names)
    return "\n".join(
        [
            method.upper(),
            uri,
            canonical_query(query),
            canonical_headers,
            signed_headers,
            sha256_hex(body_b),
        ]
    )


def build_string_to_sign(timestamp: Union[str, int], canonical_request: str) -> str:
    return "\n".join(
        ["CODO1-HMAC-SHA256", str(timestamp), sha256_hex(canonical_request.encode("utf-8"))]
    )


def sign(
    secret_key: str,
    method: str,
    uri: str,
    query: Optional[Mapping],
    headers: Mapping[str, str],
    body: Union[bytes, str, None],
    timestamp: Union[str, int],
) -> str:
    cr = build_canonical_request(method, uri, query, headers, body)
    sts = build_string_to_sign(timestamp, cr)
    return hmac_sha256_hex(secret_key, sts)


def build_auth_headers(
    access_key: str,
    secret_key: str,
    method: str,
    uri: str,
    query: Optional[Mapping] = None,
    body: Union[bytes, str, None] = None,
    content_type: Optional[str] = None,
    timestamp: Optional[Union[str, int]] = None,
    nonce: Optional[str] = None,
) -> Dict[str, str]:
    ts = str(timestamp if timestamp is not None else int(time.time()))
    n = nonce or secrets.token_hex(8)
    sign_headers = {
        "x-codo-access-key": access_key,
        "x-codo-timestamp": ts,
        "x-codo-nonce": n,
    }
    body_b = b"" if body is None else (body.encode("utf-8") if isinstance(body, str) else body)
    if content_type and body_b:
        sign_headers["content-type"] = content_type
    signature = sign(secret_key, method, uri, query, sign_headers, body_b, ts)
    out = {
        "X-Codo-Access-Key": access_key,
        "X-Codo-Timestamp": ts,
        "X-Codo-Nonce": n,
        "X-Codo-Signature": signature,
    }
    if content_type:
        out["Content-Type"] = content_type
    return out
