class Node:
    """이진트리를 위한 노드 클래스"""
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None

# 노드 인스턴스 생성
node_0 = Node(5)
node_1 = Node(3)
node_2 = Node(7)

node_0.left_child = node_1
node_0.right_child = node_2

node_1.parent = node_0
node_2.parent = node_0

# 클래스를 만들면 더 쉬움
def print_in_order(node):
    if node is not None:
        print_in_order(node.left_child)
        print(node.data)
        print_in_order(node.right_child)


class BinarySearchTree:
    """이진 탐색 트리 클래스"""
    def __init__(self):
        self.root = None

    def print_sorted_tree(self):
        print_in_order(self.root)

    def search(self, data):
        temp = self.root
        while temp is not None:
            if temp.data == data:
                return temp
            elif temp.data > data:
                temp = temp.left_child
            else:
                temp = temp.right_child
        return None

    @staticmethod
    def find_min(node):
        """(부분)이진 탐색 트리의 가장 작은 노드 리턴"""
        temp = node
        while temp.left_child is not None:
            temp = temp.left_child

        return temp

    def insert(self, data):
        new_node = Node(data)

        #트리가 비었으면 새로 root 노드를 생성
        if self.root is None:
            self.root = new_node
            return
        temp = self.root
        while temp is not None:
            if temp.data < data:
                if temp.right_child is None:
                    new_node.parent = temp
                    temp.right_child = new_node
                    return
                else:
                    temp = temp.right_child
            else:
                if temp.left_child is None:
                    new_node.parent = temp
                    temp.left_child = new_node
                    return
                else:
                    temp = temp.left_child

    def delete(self, data):
        """이진 탐색 트리 삭제 메소드"""
        node_to_delete = self.search(data)  # 삭제할 노드를 가지고 온다
        parent_node = node_to_delete.parent  # 삭제할 노드의 부모 노드

        # 지우려는 노드가 자식노드가 없는 경우
        if node_to_delete.left_child is None and node_to_delete.right_child is None:
            if node_to_delete is self.root:
                self.root = None
            else:
                if node_to_delete == parent_node.left_child:
                    parent_node.left_child = None
                else:
                    parent_node.right_child = None
        # 2. 지우려는 노드가 한개의 자식노드만 있는 경우
        elif node_to_delete.left_child is None or node_to_delete.right_child is None:
            if node_to_delete is self.root:
                if node_to_delete.left_child is None:
                    self.root = node_to_delete.right_child
                else:
                    self.root = node_to_delete.left_child
            else:
                if parent_node.left_child is node_to_delete:
                    if node_to_delete.right_child is None:
                        parent_node.left_child = node_to_delete.left_child
                        node_to_delete.left_child.parent = parent_node
                    else:
                        parent_node.left_child = node_to_delete.right_child
                        node_to_delete.right_child.parent = parent_node
                else:
                    if node_to_delete.right_child is None:
                        parent_node.right_child = node_to_delete.left_child
                        node_to_delete.left_child.parent = parent_node
                    else:
                        parent_node.right_child = node_to_delete.right_child
                        node_to_delete.right_child.parent = parent_node
        # 3. 지우려는 노드가 두개의 자식노드가 있는 경우
        else:
            successor = self.find_min(node_to_delete.right_child)
            node_to_delete.data = successor.data

            # successor 노드 트리에서 삭제
            if successor is successor.parent.left_child:
                successor.parent.left_child = successor.right_child
            else:
                successor.parent.right_child = successor.right_child
            
            if successor.right_child is not None:
                successor.right_child.parent = successor.parent



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

print(bst.search(7).data)
print(bst.search(19).data)
print(bst.search(2).data)
print(bst.search(20))

print(bst.find_min(bst.root).data)  # 전체 이진 탐색 트리에서 가장 작은 노드
print(bst.find_min(bst.root.right_child).data)  # root 노드의 오른쪽 부분 트리에서 가장 작은 노드

bst.delete(5)
bst.delete(9)

bst.print_sorted_tree()

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

# 자식이 두 개 다 있는 노드 삭제
bst.delete(7)
bst.delete(11)

bst.print_sorted_tree()