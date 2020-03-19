class Node:
    """노드 클래스"""
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    """더블리 링크드 클래스"""
    def __init__(self):
        self.head = None
        self.tail = None

    def find_node_at(self, index):
        iterator = self.head

        for _ in range(index):
            iterator = iterator.next

        return iterator

    def append(self, data):     #제일 뒤에 노드를 추가하는 메소드
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert(self, previous_node, data):  # 원하는 곳에 노드를 삽입하는 메소드
        new_node = Node(data)
        if previous_node is self.tail:  # 가장 마지막 노드 뒤에 삽입하고자 할 때
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            new_node.next = previous_node.next
            new_node.next.prev = new_node
            previous_node.next = new_node
            new_node.prev = previous_node

    def prepend(self, data):    # 가장 앞 노드 앞에 노드를 추가하는 메소드
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, node_to_delete):   # 원하는 노드를 삭제하고 해당 노드의 데이터를 리턴하는 메소드

        data = node_to_delete.data

        if node_to_delete is self.head and node_to_delete is self.tail:  # 지우려는 노드가 유일한 노드일 때
            self.head = None
            self.tail = None
        elif node_to_delete is self.head:   # 지우려는 노드가 가장 앞 노드일 경우
            self.head = self.head.next
            self.head.prev = None
        elif node_to_delete is self.tail:   # 지우려는 노드가 가장 뒤 노드일 경우
            self.tail = self.tail.prev
            self.tail.next = None
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