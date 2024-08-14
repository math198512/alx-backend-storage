#!/usr/bin/env python3
"""simple Cache class"""
import redis


class Cache:
    """simple Cache class"""
    def __init__(self) -> None:
        _redis = redis.Redis()
        _redis.flushdb()

    