class Node:
    """이진 클래스 탐색 트리 노드"""
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.right_child = None
        self.left_child = None

class BinarySearchTree:
    """이진 탐색 트리"""
    def __init__(self):
        self.root = None

    def print_sorted_tree(self):
        """이진 탐색 트리 내의 데이터를 정렬된 순서로 출려하는 메소드"""

        print_in_oder(self.root)
    def search(self, data):
        temp_node = self.root
        while temp_node is not None:
            if temp_node.data == data:
                return temp_node
            elif temp_node.data < data:
                temp_node = temp_node.right_child
            else:
                temp_node = temp_node.left_child

    def delete(self, data):
        """이진 탐색 트리 삭제 메소드"""
        node_to_delete = self.search(data)  # 삭제할 노드를 가지고 온다
        parent_node = node_to_delete.parent  # 삭제할 노드의 부모 노드

        # 경우 1: 지우려는 노드가 leaf 노드일 때 (코드를 쓰세요!)
        if node_to_delete.left_child is None and node_to_delete.right_child is None:
            if node_to_delete is self.root:
                self.root = None
            else:
                if node_to_delete == parent_node.left_child:
                    parent_node.left_child = None
                else:
                    parent_node.right_child = None
        elif node_to_delete.left_child is None:
            if node_to_delete is self.root:
                self.root = node_to_delete.right_child
                self.root.parent = None
            elif node_to_delete == parent_node.left_child:
                parent_node.left_child = node_to_delete.right_child
            else:
                parent_node.right_child = node_to_delete.right_child
            node_to_delete.right_child.parent = parent_node
        elif node_to_delete.right_child is None:
            if node_to_delete is self.root:
                self.root = node_to_delete.right_child
                self.root.parent = None
            elif node_to_delete == parent_node.left_child:
                parent_node.left_child = node_to_delete.left_child
            else:
                parent_node.right_child = node_to_delete.left_child
            node_to_delete.left_child.parent = parent_node
        else:
            successor = self.find_min(node_to_delete.right_child)
            node_to_delete.data = successor.data
            if successor.right_child is not None:
                successor.right_child.parent = successor.parent
                successor.parent.left_child = successor
            else:
                successor.parent.left_child = None

    def insert(self, data):
        new_node = Node(data)
        node = self.root
        if self.root is None:
            self.root = new_node
            return
        while new_node.parent is None:
            if node.data < new_node.data:
                if node.right_child is None:
                    node.right_child = new_node
                    new_node.parent = node
                else:
                    node = node.right_child
            elif node.data > new_node.data:
                if node.left_child is None:
                    node.left_child = new_node
                    new_node.parent = node
                else:
                    node = node.left_child

    @staticmethod
    def find_min(node):
        temp_node = node
        while temp_node.left_child is not None:
            temp_node = temp_node.left_child
        return temp_node

def print_in_oder(node):
    """주어진 node를 in-order로 출력해주는 함수"""
    if node is not None:
        print_in_oder(node.left_child)
        print(node.data)
        print_in_oder(node.right_child)



# 빈 이진 탐색 트리 생성
bst = BinarySearchTree()

# 데이터 삽입
bst.insert(7)
bst.insert(11)
bst.insert(9)
bst.insert(17)
bst.insert(8)
bst.insert(5)
bst.insert(19)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(14)

bst.delete(7)
bst.delete(11)

bst.print_sorted_tree()