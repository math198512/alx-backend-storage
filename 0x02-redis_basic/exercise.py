#!/usr/bin/env python3
"""simple Cache class"""
import redis
from uuid import uuid4
from typing import Union, Optional, Callable


UnionOfTypes = Union[str, bytes, int, float]


class Cache:
    """simple Cache class"""
    def __init__(self) -> None:
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: UnionOfTypes) -> str:
        """Store method"""
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> UnionOfTypes:
        """Reading from Redis and recovering original type"""
        if fn:
            data = fn(self._redis.get(key))
        else:
            data = self._redis.get(key)
        return data

    def get_int(self, key: str) -> int:
        """Retrieves an integer value from a Redis data storage."""
        return self.get(key: str, lambda x: int(x))

    def get_str(self, key: str) -> str:
        """Retrieves a string value from a Redis data storage."""
        return self.get(key: str, lambda x: x.decode('utf-8'))
