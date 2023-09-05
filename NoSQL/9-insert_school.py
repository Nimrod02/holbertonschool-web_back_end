#!/usr/bin/env python3
"""
module 9
"""


def insert_school(mongo_collection, **kwargs):
    """function that inserts
    a new document in a collection based on kwargs

    Args:
        mongo_collection (int): collection of object
    """
    result = mongo_collection.insert_one(kwargs)

    return result.inserted_id
