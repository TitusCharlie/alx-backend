#!/usr/bin/env python3
""" BasicCache module """


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Basic caching system without limit """

    def put(self, key, item):
        """ Assign item to the key in cache_data """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get the value linked to the key """
        return self.cache_data.get(key) if key else None
