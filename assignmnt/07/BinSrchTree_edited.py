# 코드 9.1: 이진탐색트리를 위한 노드 클래스 
class BSTNode:
    def __init__ (self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def isLeaf(self):
        return self.left is None and self.right is None

#################################################################

# rotateLL (수정됨)
def rotateLL(root):
    B = root.left
    root.left = B.right
    B.right = root
    return B  # 새로운 루트 반환

# rotateRR (수정됨)
def rotateRR(root):
    B = root.right
    root.right = B.left
    B.left = root
    return B  # 새로운 루트 반환

#################################################################

# 코드 9.2: 이진탐색트리의 탐색 연산(순환 구조)
def search_bst(n, key):
    if n is None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)

# 코드 9.3: 이진탐색트리의 탐색 연산(반복 구조)
def search_bst_iter(n, key):
    while n is not None:
        if key == n.key:
            return n
        elif key < n.key:
            n = n.left
        else:
            n = n.right
    return None

# 코드 9.4: 이진탐색트리의 값을 이용한 탐색 연산
def search_value_bst(n, value):
    if n is None:
        return None
    elif value == n.value:
        return n
    res = search_value_bst(n.left, value)
    if res is not None:
        return res
    return search_value_bst(n.right, value)

# 코드 9.5: 최대와 최소 키를 가지는 노드 탐색 연산
def search_max_bst(n):
    while n is not None and n.right is not None:
        n = n.right
    return n

def search_min_bst(n):
    while n is not None and n.left is not None:
        n = n.left
    return n

#################################################################

# 코드 9.6: 이진탐색트리의 삽입 연산(순환 구조)
def insert_bst(r, n):
    if n.key < r.key:
        if r.left is None:
            r.left = n
            return True
        else:
            return insert_bst(r.left, n)
    elif n.key > r.key:
        if r.right is None:
            r.right = n
            return True
        else:
            return insert_bst(r.right, n)
    else: 
        return False

#################################################################

# 코드 9.7: 단말노드의 삭제 연산(case1)
def delete_bst_case1(parent, node, root):
    if parent is None:  # 삭제할 단말 노드가 루트이면
        root = None  # 공백 트리가 됨
    else:
        if parent.left == node:  # 삭제할 노드가 부모의 왼쪽 자식이면
            parent.left = None  # 부모의 왼쪽 링크를 None
        else:  # 오른쪽 자식이면
            parent.right = None  # 부모의 오른쪽 링크를 None
    return root

# 코드 9.8: 자식이 하나인 노드의 삭제 연산(case2)
def delete_bst_case2(parent, node, root):
    child = node.left if node.left is not None else node.right  # child는 유효한 자식
    if node == root:  # 삭제하려는 노드가 루트이면
        root = child  # child가 새로운 루트
    else:
        if node is parent.left:
            parent.left = child  # 부모의 왼쪽 링크를 변경
        else:
            parent.right = child  # 부모의 오른쪽 링크를 변경
    return root

# 코드 9.9: 자식이 둘인 노드의 삭제 연산(case3)
def delete_bst_case3(parent, node, root):
    succp = node  # 후계자의 부모 노드
    succ = node.right  # 후계자 노드
    while succ.left is not None:  # 후계자와 부모노드 탐색
        succp = succ
        succ = succ.left
    if succp.left == succ:
        succp.left = succ.right  # 후계자의 오른쪽 자식 연결
    else:
        succp.right = succ.right  # 후계자의 왼쪽 자식 연결
    node.key = succ.key  # 후계자의 키와 값을
    node.value = succ.value  # 삭제할 노드에 복사
    return root

# 코드 9.10: 이진탐색트리의 삭제 연산
def delete_bst(root, key):
    if root is None:
        return None  # 공백 트리

    parent = None  # 삭제할 노드의 부모 탐색
    node = root  # 삭제할 노드 탐색
    while node is not None and node.key != key:
        parent = node
        if key < node.key:
            node = node.left
        else:
            node = node.right
    if node is None:
        return root  # 삭제할 노드가 없음

    # case 1: 단말 노드
    if node.left is None and node.right is None:
        root = delete_bst_case1(parent, node, root)

    # case 2: 하나의 자식을 가진 노드
    elif node.left is None or node.right is None:
        root = delete_bst_case2(parent, node, root)

    # case 3: 두 개의 자식을 가진 노드
    else:
        root = delete_bst_case3(parent, node, root)

    return root
