# heapify 알고리즘 복습
def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드1과 노드2를 바꿔주는 메소드"""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp
'''
def heapify(tree, index, index_size):
    left_child = 2 * index
    right_child = 2 * index + 1
    if right_child <= index_size and max(tree[index], tree[left_child], tree[right_child]) == tree[right_child] :
        swap(tree, index, right_child)
        heapify(tree, right_child, index_size)
    elif left_child <= index_size and max(tree[index], tree[left_child], tree[right_child]) == tree[left_child]:
        swap(tree, index, left_child)
        heapify(tree, left_child, index_size)
'''


def heapify(tree, index, tree_size):
    """heapify 함수"""

    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    largest = index  # 일단 부모 노드의 값이 가장 크다고 설정

    # 왼쪽 자식 노드의 값과 비교
    if 0 < left_child_index < tree_size and tree[largest] < tree[left_child_index]:
        largest = left_child_index

    # 오른쪽 자식 노드의 값과 비교
    if 0 < right_child_index < tree_size and tree[largest] < tree[right_child_index]:
        largest = right_child_index

    if largest != index:  # 부모 노드의 값이 자식 노드의 값보다 작으면
        swap(tree, index, largest)  # 부모 노드와 최댓값을 가진 자식 노드의 위치를 바꿔준다
        heapify(tree, largest, tree_size)  # 자리가 바뀌어 자식 노드가 된 기존의 부모 노드를대상으로 또 heapify 함수를 호출한다


tree = [None, 15, 5, 12, 14, 9, 10, 6, 2, 11, 1]  # heapify하려고 하는 완전 이진 트리
heapify(tree, 2, len(tree))  # 노드 2에 heapify 호출
print(tree)

# 힙 정렬 복습
def heapsort(tree):
    tree_size = len(tree)
    for i in range(tree_size, 0, -1):
        heapify(tree, i, tree_size)

    for i in range(1, tree_size):
        heapify(tree, 1, tree_size - i)
        swap(tree, 1, tree_size - i)

data_to_sort = [None, 6, 1, 4, 7, 10, 3, 8, 5, 1, 5, 7, 4, 2, 1]
heapsort(data_to_sort)
print(data_to_sort)


# 우선순위 큐 복습
def reverse_heapify(tree, index):
    """삽입된 노드를 힙 속성 위치로 이동시키는 함수"""
    parent_index = index // 2
    if parent_index > 0 and tree[index] > tree[parent_index]:
        swap(tree, index, parent_index)
        reverse_heapify(tree, parent_index)

class PriorityQueue:
    """힙으로 구현한 우선순위"""
    def __init__(self):
        self.heap = [None]

    def insert(self, data):
        self.heap.append(data)
        reverse_heapify(self.heap, len(self.heap) - 1)

    def extract_max(self):
        last_index = len(self.heap) - 1
        swap(self.heap, 1, last_index)
        value = self.heap.pop()
        heapify(self.heap, 1, last_index + 1)
        return value


    def __str__(self):
        return str(self.heap)

# 실행 코드
priority_queue = PriorityQueue()

priority_queue.insert(6)
priority_queue.insert(9)
priority_queue.insert(1)
priority_queue.insert(3)
priority_queue.insert(10)
priority_queue.insert(11)
priority_queue.insert(13)

print(priority_queue)


print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())