class Node:
    """링크드 리스트의 노드 클래스"""

    def __init__(self, data):
        self.data = data  #노드가 저장하는 데이터
        self.next = None  #다음 노드에 대한 레퍼런스


# 데이터 2, 3, 5, 7, 11 을 담는 노드 생성
head_node = Node(2)
node_1 = Node(3)
node_2 = Node(5)
node_3 = Node(7)
tail_node = Node(11)

# 노드들을 연결
head_node.next = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = tail_node

#노드 순서대로 출력
iterator = head_node

while iterator is not None:
    print(iterator.data)
    iterator = iterator.next

class LinkedList:
    """링크드 리스트 클래스"""
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """링크드 리스트 추가연산 메소드"""
        new_node = Node(data)
        if self.head is None: #링크드리스트 클래스가 비어있는 경우
            self.head = new_node
            self.tail = new_node
        else: #링크드리스트 클래스가 비어있지 않은 경우
            self.tail.next = new_node
            self.tail = new_node

    def find_node_at(self, index):
        """링크드 리스트 접근연산 메소드. 파라미터 인덱스는 항상 있다고 가정"""
        iterator = self.head
        for _ in range(index):
            iterator = iterator.next

        return iterator

    def insert_after(self, previous_node, data):
        """링크드 리스트 주어진 노드 뒤 데이터 삽입"""
        new_node = Node(data)

        if previous_node == self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = previous_node.next
            previous_node.next = new_node

    def delete_after(self, previous_node):
        data = previous_node.next.data

        if previous_node.next == self.tail:
            previous_node.next = None
            self.tail = previous_node
        else:
            previous_node.next = previous_node.next.next

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

# 링크드 리스트에 데이터 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(11)

node_2 = my_list.find_node_at(2)
my_list.insert_after(node_2, 6)
print(my_list)

head_node = my_list.head
my_list.insert_after(head_node, 9)
print(my_list)

print(my_list.delete_after(node_2))
print(my_list)