# 선형 큐
# 크기가 정해진 리스트의 경우
N = 10
q = [0] * N
front = -1
rear = -1

rear += 1  # enqueue(1)
q[rear] = 1
rear += 1  # enqueue(2)
q[rear] = 2
rear += 1  # enqueue(3)
q[rear] = 3

front += 1  # dequeue()
print(q[front])  # 1
front += 1  # dequeue()
print(q[front])  # 2
front += 1  # dequeue()
print(q[front])  # 3

# 빈 리스트의 경우(다른 방법)
# append pop은 시간이 오래걸리긴함. 위의 방법이 빠른 처리
q2 = []
q2.append(10)
q2.append(20)
print(q2.pop(0))  # 10
print(q2.pop(0))  # 20

#원형 큐
Q_Size = 4
cQ = [0] * Q_Size
front = rear = 0

rear = (rear+1) % Q_Size  # enq(1)
cQ[rear] = 1
rear = (rear+1) % Q_Size  # enq(2)
cQ[rear] = 2
rear = (rear+1) % Q_Size  # enq(3)
cQ[rear] = 3

front = (front+1) % Q_Size
print(cQ[front])
front = (front+1) % Q_Size
print(cQ[front])
front = (front+1) % Q_Size
print(cQ[front])

# 다시보기 참고해서 뒷부분 작성 및 확인하기

# ======================================

# 선형큐, 우선순위큐 중요
# 원형큐, 연결큐 알기만(현업에 사용. 나중에 다시 공부하게될것)

# 큐(queue)
# 원형큐, 연결큐 -> 효율성 때문에 사용
#   다른 언어에서는 큐 크기가 정해져있다.
# 원형큐: 리스트 크기를 정해놓고 돌려쓰는것
#       -> 파이썬에서는 가변 크기 설정이 가능하기 때문에 필요 x
# 연결큐: 실제 개발에 사용하는 큐
# 우선순위큐: 우선순위를 정해 뽑는 것. 커리큘럼상 아직 완벽 이해 불가능. 확인만 하고 넘어가기

# 연결 큐
q = [5, 3, 2, 1, 4]

# 파이썬 리스트는 매우 강력하다!
# 언제 많이 써야할까?
# - 데이터 조회를 많이 할 때 (인덱스 위치만 알면 바로 조회 가능)
#   ex. 리스트 한번 완성시켜놓고, 여러 번 조회를 하는 문제들
# 언제 사용을 피해야할까?
# - 데이터 삽입/삭제가 많을 때 (특히 삭제)
# - 이유: 속도(시간)때문. append O(1~N), pop O(N)
# - 이 경우 append, pop 대신 어려운 방식(ex. front/rear) 같은 것을 사용해야한다.

# 그렇다면 실제 개발에서는 어떻게 하나?
# 연결리스트(Linked List) 이용
# - 각 노드(데이터)가 다음 노드를 가리키는 형태를 가진 자료구조
# - 특징
#   - 메모리가 떨어져서 저장된다.
#   - 조회 시에는 리스트에 비해 느리다.
#     - Head(시작점)부터 순차적으로 접근하며 탐색하는 형태로 사용되기 때문
#   - 삽입/삭제 연산이 매우 효율적이다.
#     - 삭제: 삭제하고자 하는 노드의 이전 노드가 가리키는 것을
#            다음 노드로 바꿔주기만 하면 된다.
#        -> 연산 한 번 만에 끝난다.
#     - 삭제할 때, 메모리가 비효율적으로 관리되지 않나요?
#        - "메모리 누수"가 발생한다!
#        -> 사용하지 않는 메모리를 회수하는 동작:
#               가비지 컬렉션(Garbage Collection; GC) 이라고 한다.
#        - 놀라운 파이썬: None 으로 할당하면, 메모리 자동으로 삭제!!
#     - 삽입: 추가하고자 하는 NEW 노드의 이전 노드가 가리키는 것을
#            NEW 노드로 바꿔주고, NEW 노드의 다음 노드를
#            원래 이전 노드가 바라보고 있던 노드로 설정해준다.
#        -> 연산 1~2번이면 된다.(그림으로 외우자)

# 구글링을 통해 삽입, 삭제 연산 그림을 보시고 코드 분석 하시는 것을 추천 드립니다.


class Node:
    def __init__(self, data):
        self.data = data  # 노드의 데이터
        self.next = None  # 다음 노드에 대한 포인터


class LinkedList:
    def __init__(self):
        self.head = None  # 연결 리스트의 시작점(헤드)

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def delete_node(self, key):
        # 헤드가 삭제할 노드인 경우
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next  # 헤드를 다음 노드로 변경
                temp = None  # 기존 헤드 노드를 삭제
                return

        # 삭제할 노드를 탐색
        prev = None
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # 노드가 리스트에 없는 경우
        if temp is None:
            print(f"Node with data {key} not found.")
            return

        # 노드를 리스트에서 제거
        prev.next = temp.next
        temp = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# 연결 리스트 사용 예시
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.print_list()  # 출력: 1 -> 2 -> 3 -> 4 -> None

llist.delete_node(2)
llist.print_list()  # 출력: 1 -> 3 -> 4 -> None

llist.delete_node(4)
llist.print_list()  # 출력: 1 -> 3 -> None

llist.delete_node(5)  # 출력: Node with data 5 not found.


# 덱(deque)
# 내부적으로 "이중 연결리스트"로 구현되어있다.
# 연결 리스트에 비해 화살표만 조금 더 건드려주면 된다!
# 즉, 연결 리스트의 장점을 그대로 가지고 있으면서 뒤에서부터 조회가 가능하다!

# 데이터가 클수록 덱 사용
# 데이터가 작으면 (수정이 적고 조회가 많다) 리스트 사용

from collections import deque

# 리스트와 다른 점
dq = deque()  # 1. 선언할 때 deque()으로 해야한다.
dq.append(3)
dq.append(5)
dq.appendleft(4)  # 2. appendleft 가 더 효율적이다.

dq.pop()
dq.popleft()  # 3. pop 도 더 효율적이다.

# 단점. index 조회가 안 된다!


