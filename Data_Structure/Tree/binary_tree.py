class Node:
    """이진 트리 노드 클래스"""

    def __init__(self, data):
        """데이터와 두 자식에 대한 레퍼런스를 갖는다"""
        self.data = data
        self.left_child = None
        self.right_child = None


root_node = Node("A")
node_B = Node("B")
node_C = Node("C")

root_node.left_child = node_B
root_node.right_child = node_C

node_D = Node("D")
node_E = Node("E")

node_B.left_child = node_D
node_B.right_child = node_E

node_F = Node("F")

node_C.right_child = node_F

node_G = Node("G")
node_H = Node("H")

node_E.left_child = node_G
node_E.right_child = node_H

print(node_F.data)
print(node_G.data)
print(node_H.data)


