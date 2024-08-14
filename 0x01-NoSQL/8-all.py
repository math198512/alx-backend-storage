#!/usr/bin/env python3
"""a Python fupip3 install pymongonction that lists all documents in a collection"""
import pymongo


def list_all(mongo_collection):
    """a Python function that lists all documents in a collection"""
    if not mongo_collection:
        return []
    return mongo_collection.find()
