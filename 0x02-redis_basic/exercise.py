#!/usr/bin/env python3
"""simple Cache class"""
import redis
from uuid import uuid4
from typing import Union, Optional, Callable
from functools import wraps


UnionOfTypes = Union[str, bytes, int, float]

def count_calls(method: Callable) -> Callable:
    """TO DO"""
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> any:
        """here"""
        self._redis.incr(method.__qualname__)

        return method(self, *args, **kwargs)
    return wrapper

class Cache:
    """simple Cache class"""
    def __init__(self) -> None:
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
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
        return self.get(key, lambda x: int(x))

    def get_str(self, key: str) -> str:
        """Retrieves a string value from a Redis data storage."""
        return self.get(key, lambda x: x.decode('utf-8'))
