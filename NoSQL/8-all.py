#!/usr/bin/env python3
"""
module 8
"""


def list_all(mongo_collection):
    """
    Python function that lists all documents in a collection
    """
    return list(mongo_collection.find())


