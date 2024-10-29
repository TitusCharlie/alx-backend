#!/usr/bin/env python3
""" LRUCache module """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRU caching system with a limit """

    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add item to cache using LRU policy """
        if key and item:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.order.pop(0)
                print(f"DISCARD: {lru_key}")
                del self.cache_data[lru_key]
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get value linked to the key and update access order """
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
