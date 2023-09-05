#!/usr/bin/env python3
"""
module 11
"""


def schools_by_topic(mongo_collection, topic):
    """ function that returns
    the list of school having a specific topic

    Args:
        mongo_collection (collection): pymongo collection object
        topic (str): will be topic searched
    """
    list_collec = mongo_collection.list_collection_names()

    return list_collec
