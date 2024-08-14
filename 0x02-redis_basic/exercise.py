#!/usr/bin/env python3
"""simple Cache class"""
import redis
from uuid import uuid4


class Cache:
    """simple Cache class"""
    def __init__(self) -> None:
          """Constructor"""
          self._redis = redis.Redis()
          self._redis.flushdb()

    def Store(self, data) -> str:
        """Store method"""
        key = str(uuid4())
        self._redis.mset({key: data})
        return key
         
    