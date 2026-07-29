#!/usr/bin/env python
# -*- coding: utf-8 -*-
from websdk2.openapi_sign import build_auth_headers, sign


def test_get_vector():
    ak = "codoAKTEST0001"
    sk = "testSecretKeyForOpenAPISign0001"
    ts = "1700000000"
    nonce = "nonce-fixed-001"
    headers = {
        "x-codo-access-key": ak,
        "x-codo-timestamp": ts,
        "x-codo-nonce": nonce,
    }
    sig = sign(sk, "GET", "/api/p/v4/biz/list/", {}, headers, b"", ts)
    assert sig == "ce94e413a8f752ed75a7c129c184f14892d8b24f30222607994276174339e07f"


def test_post_vector():
    ak = "codoAKTEST0001"
    sk = "testSecretKeyForOpenAPISign0001"
    ts = "1700000000"
    nonce = "nonce-fixed-001"
    headers = {
        "content-type": "application/json",
        "x-codo-access-key": ak,
        "x-codo-timestamp": ts,
        "x-codo-nonce": nonce,
    }
    body = b'{"page":1}'
    sig = sign(sk, "POST", "/api/p/v4/user/", {}, headers, body, ts)
    assert sig == "4a2adef69ff58b92bc99c04474811e78082a5e3f5675a3c1d26e19ed3e7dc163"


def test_build_auth_headers_keys():
    h = build_auth_headers(
        "ak", "sk", "GET", "/api/x/", query=None, body=None, timestamp=1700000000, nonce="n1"
    )
    assert "X-Codo-Access-Key" in h
    assert "X-Codo-Signature" in h
