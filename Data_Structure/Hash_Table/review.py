class Node:
    """노드 클래스"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LinkedList:
    """더블리 링크드리스트 클래스"""
    def __init__(self):
        self.head = None
        self.tail = None

    def find_node_with_key(self, key):
        """key를 이용해 원하는 노드를 찾는 클래스"""
        iterator = self.head
        while iterator is not None:
            if iterator.key == key:

                return iterator
            iterator = iterator.next

        return None

    def append(self, key, value):
        """링크드 리스트 맨 뒤에 새로운 노드를 추가하는 클래스"""
        new_node = Node(key, value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete(self, node_to_delelte):
        """원하는 노드를 삭제하는 클래스"""
        data = node_to_delelte.value
        if node_to_delelte is self.head and node_to_delelte is self.tail:
            self.head = None
            self.tail = None
        elif node_to_delelte is self.head:
            self.head = self.head.next
            self.head.prev = None
        elif node_to_delelte is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node_to_delelte.prev.next = node_to_delelte.next
            node_to_delelte.next.prev = node_to_delelte.prev

        return data

    def __str__(self):
        res_str = ""
        iterator = self.head

        while iterator is not None:
            res_str += "{} : {}\n".format(iterator.key, iterator.value)
            iterator = iterator.next

        return res_str

class HashTable:
    def __init__(self, capacity):
        self._capacity = capacity
        self._table = [LinkedList() for _ in range(self._capacity)]

    def _hash_function(self, key):
        return hash(key) % self._capacity

    def _get_linked_list_for_key(self, key):
        hashed_key = self._hash_function(key)
        return self._table[hashed_key]

    def _look_up_node(self, key):
        linked_list = self._get_linked_list_for_key(key)
        return linked_list.find_node_with_key(key)


    def look_up_value(self, key):
        return self._look_up_node(key).value


    def insert(self, key, value):

        temp = self._look_up_node(key)

        if temp is not None:
            temp.value = value
        else:
            self._get_linked_list_for_key(key).append(key, value)

    def delete_by_key(self, key):
        linked_list = self._get_linked_list_for_key(key)
        temp = self._look_up_node(key)
        if temp is not None:
            linked_list.delete(temp)

    def __str__(self):
        res_str = ""

        for linked_list in self._table:
            res_str += str(linked_list)

        return res_str[:-1]


test_scores = HashTable(50) # 시험 점수를 담을 해시 테이블 인스턴스 생성

# 여러 학생들 이름과 시험 점수 삽입
test_scores.insert("현승", 85)
test_scores.insert("영훈", 90)
test_scores.insert("동욱", 87)
test_scores.insert("지웅", 99)
test_scores.insert("신의", 88)
test_scores.insert("규식", 97)
test_scores.insert("태호", 90)

# 학생들 시험 점수 삭제
test_scores.delete_by_key("태호")
test_scores.delete_by_key("지웅")
test_scores.delete_by_key("신의")
test_scores.delete_by_key("현승")
test_scores.delete_by_key("규식")

print(test_scores)