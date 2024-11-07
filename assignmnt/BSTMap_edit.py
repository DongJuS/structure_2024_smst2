''' 이진 탐색 트리를 이용한 맵 프로그램을 구현하시오.
- 교재의 이진 탐색 트리 예제 프로그램과 맵 클래스 함수를 사용하여, 맵 클래스 함수를 
아래 조건으로 수정하시오.- 맵 클래스의 display 메소드의 파라미터에 ‘order’를 추가하고, order = 1 인 경우, 
inorder, 2 인 경우 preorder, 3 인 경우 postorder 가 될 수 있도록 수정하시오. 예) 
display(self, msg = ‘BSTMap :’, order).- 테스트 프로그램은 347쪽 (코드 9.9) 를 수정하여 트리 순회 방식에 따른 순회 결과를 출
력하시오'''
# 2024-11-07
# 작성자 : 서동주

from BinSrchTree import *

def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.key, end=' ')
        inorder(n.right)

def preorder(n):
    if n is not None:
        print(n.key, end=' ')
        preorder(n.left)
        preorder(n.right)

def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.key, end=' ')

# 코드 9.11: 이진탐색트리를 이용한 맵 클래스
class BSTMap():
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root == None

    def findMax(self):
        return search_max_bst(self.root)

    def findMin(self):
        return search_min_bst(self.root)

    def search(self, key):
        return search_bst(self.root, key)

    def searchValue(self, key):
        return search_value_bst(self.root, key)

    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            insert_bst(self.root, n)

    def delete(self, key):
        self.root = delete_bst(self.root, key)

    def display(self, msg='BSTMap :', order=1):
        print(msg, end='')
        if order == 1:
            inorder(self.root)
        elif order == 2:
            preorder(self.root)
        elif order == 3:
            postorder(self.root)
        else:
            print("Invalid order")
        print()

#=========================================================
# 코드 9.12: 이진탐색트리를 이용한 맵 테스트 프로그램
if __name__ == "__main__":
    data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]
    value= ["삼오", "일팔", "영칠", "이육", "일이", "영삼", "육팔", "이이", "삼영", "구구"]

    map = BSTMap()
    map.display("[삽입 전] : ")
    for i in range(len(data)):
        map.insert(data[i], value[i])
        map.display(f"[삽입 {data[i]:2d}] : ")

    print('[최대 키] : ', map.findMax().key)
    print('[최소 키] : ', map.findMin().key)
    print('[탐색 26] : ', '성공' if map.search(26) != None else '실패')
    print('[탐색 25] : ', '성공' if map.search(25) != None else '실패')
    print('[탐색 일팔]:', '성공' if map.searchValue("일팔") != None else '실패')
    print('[탐색 일칠]:', '성공' if map.searchValue("일칠") != None else '실패')
    
    map.delete(3)
    map.display("[삭제  3] : ")
    map.delete(68)
    map.display("[삭제 68] : ")
    map.delete(18) 
    map.display("[삭제 18] : ")
    map.delete(35) 
    map.display("[삭제 35] : ")

    # 트리 순회 방식에 따른 결과 출력
    print("\nInorder Traversal:")
    map.display(order=1)

    print("\nPreorder Traversal:")
    map.display(order=2)

    print("\nPostorder Traversal:")
    map.display(order=3)
