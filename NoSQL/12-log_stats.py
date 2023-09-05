#!/usr/bin/env python3
"""
module 12
"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs.ngix

    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    count_logs = db.count_documents({})
    print(f"{count_logs} logs")

    print("Methods:")
    for method in methods:
        count_method = db.count_documents({"method": method})
        print(f"\tmethod {method}: {count_method}")

    check = db.count_documents({"method": "GET", "path": "/status"})

    print(f"{check} status check")
