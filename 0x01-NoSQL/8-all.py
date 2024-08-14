#!/usr/bin/env python3
"""a Python function that lists all documents in a collection"""
import pymongo


def list_all(mongo_collection):
    """a Python function that lists all documents in a collection"""
    if not mongo_collection:
        return []
    return mongo_collection.find()
if __name__ == '__main__':
    list_all(mongo_collection)
