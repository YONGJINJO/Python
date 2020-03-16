class Node:
    """딕셔너리를 위한 이진탐색트리 노드"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.parent = None
        self.right_child = None
        self.left_child = None