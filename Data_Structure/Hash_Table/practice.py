class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def find_with_key(self, key):
        iterator = self.head

        while iterator is not None:
            if iterator.key == key:
                return iterator
            iterator = iterator.next

        return None

    def append(self, key, value):
        new_node = Node(key, value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            new_node =self.tail

    def delete(self, node_to_delete):
        data = node_to_delete.value

        if node_to_delete is self.tail and node_to_delete is self.head:
            self.tail = None
            self.head = None
        elif node_to_delete is self.tail:
            self.tail.prev = self.tail
            self.tail.next = None
        elif node_to_delete is self.head:
            self.head.next = self.head
            self.head.prev = None
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

        return data

    def __str__(self):
        res_str = ""
        iterator = self.head
        while iterator is not None:
            res_str += "{} : {}".format(iterator.key, iterator.value)
            iterator = iterator.next

        return res_str