def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다"""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp


def heapify(tree, index, tree_size):
    """heapify 함수"""

    left_child_index = 2 * index
    right_child_index = 2 * index + 1
    largest = index
    if left_child_index < tree_size and tree[left_child_index] > tree[largest]:
        largest = left_child_index

    if right_child_index < tree_size and tree[right_child_index] > tree[largest]:
        largest = right_child_index
    if largest != index:
        swap(tree, largest, index)
        heapify(tree, largest, tree_size)

def reverse_heapify(tree, index):
    """삽입된 노드를 힙 속성을 지키는 위치로 이동시키는 함수"""
    parent_index = index // 2  # 삽입된 노드의 부모 노드의 인덱스 계산

    # 부모 노드가 존재하고, 부모 노드의 값이 삽입된 노드의 값보다 작을 때
    if 0 < parent_index < len(tree) and tree[index] > tree[parent_index]:
        swap(tree, index, parent_index)  # 부모 노드와 삽입된 노드의 위치 교환
        reverse_heapify(tree, parent_index)  # 삽입된 노드를 대상으로 다시 reverse_heapify 호출



''' 
    if index > tree_size - 1:
        return tree
    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
    left_child_index = 2 * index
    right_child_index = 2 * index + 1
    if left_child_index > tree_size - 1 and right_child_index > tree_size - 1:
        return tree
    elif right_child_index > tree_size - 1:
        if tree[index] < tree[left_child_index]:
            swap(tree, index, left_child_index)
    else:
        if max(tree[index], tree[left_child_index], tree[right_child_index]) == tree[right_child_index]:
            swap(tree, index, right_child_index)
        elif max(tree[index], tree[left_child_index], tree[right_child_index]) == tree[left_child_index]:
            swap(tree, index, left_child_index)
    heapify(tree, left_child_index, tree_size)
    heapify(tree, right_child_index, tree_size)
'''
