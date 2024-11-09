from BinaryTree import *
from BinSrchTree import *

def calc_height(n):
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    return max(hLeft, hRight) + 1

def calc_height_diff(n):
    if n is None:
        return 0
    return calc_height(n.left) - calc_height(n.right)

# 수정된 rotateLL 함수
def rotateLL(A):
    B = A.left
    A.left = B.right
    B.right = A
    return B

# 수정된 rotateRR 함수
def rotateRR(A):
    B = A.right
    A.right = B.left
    B.left = A
    return B

def rotateRL(A):
    B = A.right
    A.right = rotateLL(B)
    return rotateRR(A)

def rotateLR(A):
    B = A.left
    A.left = rotateRR(B)
    return rotateLL(A)

def reBalance(parent):
    hDiff = calc_height_diff(parent)

    if hDiff > 1:
        if calc_height_diff(parent.left) > 0:
            parent = rotateLL(parent)
        else:
            parent = rotateLR(parent)
    elif hDiff < -1:
        if calc_height_diff(parent.right) < 0:
            parent = rotateRR(parent)
        else:
            parent = rotateRL(parent)
    return parent

# AVL 트리의 삽입 연산
def insert_avl(parent, node):
    if node.key < parent.key:
        if parent.left:
            parent.left = insert_avl(parent.left, node)
        else:
            parent.left = node
        return reBalance(parent)

    elif node.key > parent.key:
        if parent.right:
            parent.right = insert_avl(parent.right, node)
        else:
            parent.right = node
        return reBalance(parent)
    else:
        print("중복된 키 에러")

# AVL 트리의 삭제 연산
def delete_avl(root, key):
    if root is None:
        return None

    if key < root.key:
        root.left = delete_avl(root.left, key)
    elif key > root.key:
        root.right = delete_avl(root.right, key)
    else:
        # 노드 삭제 로직
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            # 오른쪽 서브트리에서 가장 작은 노드를 찾아 교체
            min_larger_node = root.right
            while min_larger_node.left:
                min_larger_node = min_larger_node.left
            root.key = min_larger_node.key
            root.right = delete_avl(root.right, min_larger_node.key)

    return reBalance(root)

# Level-order traversal
from CircularQueue import CircularQueue

def levelorder(root):
    queue = CircularQueue(100)
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.key, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

# AVL 트리 테스트 프로그램
if __name__ == "__main__":
    node = [7, 8, 9, 2, 1, 5, 3, 6, 4]
    root = None
    for i in node:
        n = BSTNode(i)
        if root is None:
            root = n
        else:
            root = insert_avl(root, n)
        print("AVL(%d): " % i, end='')
        levelorder(root)
        print()

    print("\n삭제 연산 수행 후 트리 상태:")
    for key in [4, 7, 9]:  # 삭제할 키들
        print(f"\n삭제({key}):", end=' ')
        root = delete_avl(root, key)
        levelorder(root)
        print()

    print("노드의 개수 =", count_node(root))
    print("단말의 개수 =", count_leaf(root))
    print("트리의 높이 =", calc_height(root))
