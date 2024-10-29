#!/usr/bin/env python3
""" MRUCache module """

from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """ MRU caching system with a limit """

    def __init__(self):
        super().__init__()
        self.most_recent = None

    def put(self, key, item):
        """ Add item to cache using MRU policy """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print(f"DISCARD: {self.most_recent}")
                del self.cache_data[self.most_recent]
            self.cache_data[key] = item
            self.most_recent = key

    def get(self, key):
        """ Get value linked to the key and update MRU """
        if key in self.cache_data:
            self.most_recent = key
            return self.cache_data[key]
        return None