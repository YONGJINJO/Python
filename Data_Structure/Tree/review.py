class Node:
    """이진 트리 노드 클래스"""
    def __init__(self, data):
        """데이터와 두 자식 노드에 대한 레퍼런스를 갖는다."""
        self.data = data
        self.left_child = None
        self.right_child = None


root_node = Node(2)
node_1 = Node(3)
node_2 = Node(5)
node_3 = Node(7)
node_4 = Node(11)

root_node.left_child = node_1
root_node.right_child = node_2
node_1.left_child = node_3
node_1.right_child = node_4

print(node_1.left_child.data)


# 완전이진 트리를 파이썬 리스트를 이용해 구현하기
complete_binary_tree = [None, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("완전 이진 트리 파이썬 리스트를 이용해 구현하는 것 review")

def get_parent_index(complete_binary_tree, index):
    """완전 이진 트리에서 index번째 노드의 부모 노드의 인덱스를 리턴하는 함수"""
    if index > len(complete_binary_tree) - 1:
        return None
    elif index < 2:
        return None
    else:
        return index // 2

def get_left_child_index(complete_binary_tree, index):
    """완전 이진 트리에서 index번째 노드의 왼쪽 자식 노드의 인덱스를 리턴하는 함수"""
    left_child_index = index * 2
    if left_child_index > len(complete_binary_tree) - 1:
        return None
    else:
        return left_child_index

def get_right_child_index(complete_binary_tree, index):
    """완전 이진 트리에서 index번째 노드의 오른쪽 자식 노드의 인덱스를 리턴하는 함수"""
    right_child_index = index * 2 + 1
    if right_child_index > len(complete_binary_tree) - 1:
        return None
    else:
        return right_child_index

# 실행 코드
root_node_index = 1 # root 노드

tree = [None, 1, 5, 12, 11, 9, 10, 14, 2, 10]  # 과제 이미지에 있는 완전 이진 트리

# root 노드의 왼쪽과 오른쪽 자식 노드의 인덱스를 받아온다
left_child_index = get_left_child_index(tree, root_node_index)
right_child_index = get_right_child_index(tree,root_node_index)

print(tree[left_child_index])
print(tree[right_child_index])

# 9번째 노드의 부모 노드의 인덱스를 받아온다
parent_index = get_parent_index(tree, 9)

print(tree[parent_index])

# 부모나 자식 노드들이 없는 경우들
parent_index = get_parent_index(tree, 1)  # root 노드의 부모 노드의 인덱스를 받아온다
print(parent_index)

left_child_index = get_left_child_index(tree, 6)  # 6번째 노드의 왼쪽 자식 노드의 인덱스를 받아온다
print(left_child_index)

right_child_index = get_right_child_index(tree, 8)  # 8번째 노드의 오른쪽 자식 노드의 인덱스를 받아온다
print(right_child_index)


# 트리 순회 복습
print("트리 순회 review")

def traverse_inorder(node):
    """in-order 순회 함수"""
    if node is not None:
        traverse_inorder(node.left_child)
        print(node.data)
        traverse_inorder(node.right_child)


node_A = Node("A")
node_B = Node("B")
node_C = Node("C")
node_D = Node("D")
node_E = Node("E")
node_F = Node("F")
node_G = Node("G")
node_H = Node("H")
node_I = Node("I")

# 생성한 노드 인스턴스들 연결
node_F.left_child = node_B
node_F.right_child = node_G

node_B.left_child = node_A
node_B.right_child = node_D

node_D.left_child = node_C
node_D.right_child = node_E

node_G.right_child = node_I

node_I.left_child = node_H

# 노드 F를 root 노드로 만든다
root_node = node_F

# 만들어 놓은 트리를 in-order로 순회한다
traverse_inorder(root_node)