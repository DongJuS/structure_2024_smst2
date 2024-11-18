class CircularQueue:
    def __init__(self, capacity=10):  # 용량을 10으로 변경
        self.capacity = capacity        # 용량(고정)
        self.array = [None] * capacity  # 요소들을 저장할 배열
        self.front = 0                  # 전단의 인덱스
        self.rear = 0                   # 후단의 인덱스

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]

    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]

    # 코드 5.2: 큐의 전체 요소의 수 계산
    def size( self ) :
       return (self.rear - self.front + self.capacity) % self.capacity

    # 코드 5.3: 문자열 변환을 위한 str 연산자 중복
    def __str__(self):
        if self.front < self.rear :
            return str(self.array[self.front+1:self.rear+1])
        else :
            return str(self.array[self.front+1:self.capacity] + \
                       self.array[0:self.rear+1] )

# 테스트 프로그램
if __name__ == "__main__":
    q = CircularQueue(10)  # capacity를 10으로 설정
    while True:
        command = input("명령어 입력 (e: enqueue, d: dequeue, q: quit): ")
        if command == 'e':
            item = input("추가할 요소 입력: ")
            q.enqueue(item)
            print("enqueue 수행 후 큐 상태:", q)
        elif command == 'd':
            removed_item = q.dequeue()
            if removed_item is not None:
                print("dequeue 수행 후 삭제된 요소:", removed_item)
            else:
                print("큐가 비어 있습니다.")
            print("dequeue 수행 후 큐 상태:", q)
        elif command == 'q':
            break
        else:
            print("잘못된 명령어입니다. 다시 입력하세요.")
