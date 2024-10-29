#!/usr/bin/env python3
""" LIFOCache module """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO caching system with a limit """

    def __init__(self):
        super().__init__()
        self.last = None

    def put(self, key, item):
        """ Add item to cache using LIFO policy """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                            and key not in self.cache_data:
                print(f"DISCARD: {self.last}")
                del self.cache_data[self.last]
            self.cache_data[key] = item
            self.last = key

    def get(self, key):
        """ Get value linked to the key """
        return self.cache_data.get(key) if key else None
