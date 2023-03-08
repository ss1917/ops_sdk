import json
from tornado.httpclient import HTTPRequest, AsyncHTTPClient
from tornado.gen import coroutine


@coroutine
def fetch_coroutine(url, method='GET', body=None, **kwargs):
    request = HTTPRequest(url, method=method, body=body, connect_timeout=5, request_timeout=10)
    http_client = AsyncHTTPClient(**kwargs)
    response = yield http_client.fetch(request)
    body = json.loads(response.body)
    return body