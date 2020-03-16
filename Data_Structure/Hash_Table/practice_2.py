from practice import LinkedList

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [LinkedList() for _ in range(self.capacity)]

    def _hash_function(self, key):
        return hash(key) % self.capacity

    def _find_table(self, key):
        hashed_index = self._hash_function(key)
        return self.table[hashed_index]

    def find_node(self, key):
        linked_list = self._find_table(key)
        return linked_list.find_with_key(key)

    def look_up_value(self, key):

        return self.find_node(key).value



