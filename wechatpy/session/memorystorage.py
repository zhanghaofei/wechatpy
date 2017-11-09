# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import time
from wechatpy.session import SessionStorage


class MemoryStorage(SessionStorage):

    def __init__(self):
        self._data = {}

    def get(self, key, default=None):
        default = dict(token='', expires_in=0, update_time=0, expire_at=0)
        token = self._data.get(key, default)
        return token['token'], ['token.expires_at']

    def set(self, key, value, expires_in=0):
        now = int(time.time())
        token = dict(token=value, expires_in=expires_in, update_time=now, expire_at=now + expires_in)
        self._data[key] = token

    def delete(self, key):
        self._data.pop(key, None)
