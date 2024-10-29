#!/usr/bin/env python3
""" FIFOCache module """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching system with a limit """

    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add item to cache using FIFO policy """
        if key and item:
            if key not in self.cache_data and len(
                                self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = self.order.pop(0)
                print(f"DISCARD: {first_key}")
                del self.cache_data[first_key]
            self.cache_data[key] = item
            if key not in self.order:
                self.order.append(key)

    def get(self, key):
        """ Get value linked to the key """
        return self.cache_data.get(key) if key else None
