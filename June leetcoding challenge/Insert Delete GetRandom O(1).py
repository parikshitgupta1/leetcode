import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list_ds = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.list_ds:
            self.list_ds.append(val)
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.list_ds:
            self.list_ds.remove(val)
            return True 
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.list_ds)
