class Node:
    """링크드 리스트의 노드 클래스"""

    def __init__(self, data):
        self.data = data  #노드가 저장하는 데이터
        self.next = None  #다음 노드에 대한 레퍼런스
        self.prev = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def find_node_at(self, index):
        """링크드 리스트 접근연산 메소드. 파라미터 인덱스는 항상 있다고 가정"""
        iterator = self.head
        for _ in range(index):
            iterator = iterator.next

        return iterator

    def find_node_with_data(self, data):
        """링크드 리스트에서 탐색 연산 메소드. 단, 해당 노드가 없으면 None을 리턴한다"""
        iterator = self.head
        while iterator is not None:
            if iterator.data == data:
                return iterator
            else:
                iterator = iterator.next

        return None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert_after(self, previous_node, data):
        new_node = Node(data)
        if previous_node == self.tail:
            previous_node.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            new_node.next = previous_node.next
            new_node.prev = previous_node
            previous_node.next = new_node
            new_node.next.prev = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def delete(self, node_to_delete):
        data = node_to_delete.data
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.head = None
            self.tail = None
        elif node_to_delete is self.head:
            self.head = node_to_delete.next
            self.head.prev = None
        elif node_to_delete is self.tail:
            self.tail = node_to_delete.prev
            self.tail.next = None
        else:
            node_to_delete.next.prev = node_to_delete.prev
            node_to_delete.prev.next = node_to_delete.next

        return data

    def __str__(self):
        """링크드 리스트를 문자열로 표현하는 메소드"""
        res_str = "|"
        iterator = self.head
        while iterator is not None:
            res_str += " {} |".format(iterator.data)
            iterator = iterator.next

        return res_str

my_list = LinkedList()

# 새로운 노드 4개 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)

print(my_list)

# 두 노드 사이에 있는 노드 삭제
node_at_index_2 = my_list.find_node_at(2)
my_list.delete(node_at_index_2)
print(my_list)

# 가장 앞 노드 삭제
head_node = my_list.head
print(my_list.delete(head_node))
print(my_list)

# 가장 뒤 노드 삭제
tail_node = my_list.tail
my_list.delete(tail_node)
print(my_list)

# 마지막 노드 삭제
last_node  = my_list.head
my_list.delete(last_node)
print(my_list)
