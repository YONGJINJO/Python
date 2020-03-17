class Node:
    """해쉬테이블을 위한 노드 클래스"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    """링크드 리스트 클래스"""
    def __init__(self):
        self.head = None
        self.tail = None

    def find_node_with_key(self, key):
        """key를 이용하여 원하는 node를 찾는 함수, node가 존재하지 않으면 None 리턴"""
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
            self.tail = new_node

    def delete(self, node_to_delete):
        """지정된 노드를 삭제하는 메소드, 삭제한 노드의 value를 리턴"""
        if node_to_delete == self.head and node_to_delete == self.tail: #지우려는 노드가 마지막으로 남은 노드일 경우
            self.head = None
            self.tail = None
        elif node_to_delete == self.head: # 지우려는 노드가 head 노드일 경우
            self.head.next = self.head
            self.head.prev = None
        elif node_to_delete == self.tail: # 지우려는 노드가 tail 노드일 경우
            self.tail.prev = self.tail
            self.tail.next = None
        else: # 지우려는 노드가 사이에 존재하는 임의의 노드일 경우
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

        return node_to_delete.value

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴"""

        res_str = ""
        iterator = self.head
        while iterator is not None:
            res_str += "{} : {}".format(iterator.key, iterator.value)
            iterator = iterator.next
        return res_str