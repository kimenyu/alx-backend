#!/usr/bin/python3
class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")


class BasicCache(BaseCaching):
    """ Defines the BasicCache class that inherits from BaseCaching.
    """

    def put(self, key, item):
        """assigns the value of the key to the dictionary

        Args:
            key (key): dictionary key
            item (item): dictionary item
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
    
    def get(self, key):
        """ Get an item from the cache. 
        If key is None or key doesn't exist in the cache, return None.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
