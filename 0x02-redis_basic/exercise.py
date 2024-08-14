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
