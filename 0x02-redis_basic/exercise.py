#!/usr/bin/env python3
"""simple Cache class"""
import redis


class Cache:
    """simple Cache class"""
    def __init__(self) -> None:
          """Constructor"""
          self._redis = redis.Redis()
          self._redis.flushdb()

    