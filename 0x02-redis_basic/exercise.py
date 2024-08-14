#!/usr/bin/env python3
"""simple Cache class"""
import redis
from uuid import uuid4
from typing import Union, Optional, Callable
from functools import wraps


UnionOfTypes = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """count the number of calls for a method"""
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> any:
        """count wrapper"""
        self._redis.incr(method.__qualname__)

        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """gives history of inputs and outputs for method"""
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> any:
        """call_history wrapper"""
        in_key = '{}:inputs'.format(method.__qualname__)
        out_key = '{}:outputs'.format(method.__qualname__)
        self._redis.rpush(in_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(in_key, str(args))
        return output
    return wrapper


class Cache:
    """simple Cache class"""
    def __init__(self) -> None:
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
