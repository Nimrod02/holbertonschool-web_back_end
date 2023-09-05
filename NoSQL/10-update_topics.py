#!/usr/bin/env python3
"""
module 10
"""


def update_topics(mongo_collection, name, topics):
    """ function that changes all topics
    of a school document based on the name

    Args:
        mongo_collection (collection): collection object
        name (str): school name to update
        topics (list[str]): list of topics
    """
    filter = {"name": name}
    new_query = {"$set": {"topics": topics}}

    update_result = mongo_collection.update_many(filter, new_query)

    return update_result
