from collections import deque

class CustomerComplaint:
    """고객 센터 문의를 나타내는 클래스"""
    def __init__(self, name, email, content):
        self.name = name
        self.email = email
        self.content = content

class CustomerServiceCenter:
    """호텔 서비스 센터 클래스"""
    def __init__(self):
        self.queue = deque()

    def process_complaint(self):
        """접수된 고객센터 문의 내용 처리하는 메소드"""
        if self.queue:
            complaint = self.queue.popleft()
            print("{}님의 {} 문의 내용 접수 되었습니다. 담당자가 배정되면 {}로 연락드리겠습니다!".format(complaint.name, complaint.content, complaint.email))
        else:
            print("더 이상 대기 중인 문의가 없습니다!")

    def add_complaint(self, name, email, content):
        """새로운 문의를 큐에 추가시켜주는 메소드"""
        complaint = CustomerComplaint(name, email, content)
        self.queue.append(complaint)

# 큐 관련 리뷰
print("queue 복습")

# 고객 문의 센터 인스턴스 생성
center = CustomerServiceCenter()

# 문의 접수한다
center.add_complaint("강영훈", "younghoon@codeit.com", "음식이 너무 맛이 없어요")

# 문의를 처리한다
center.process_complaint()
center.process_complaint()

# 문의 세 개를 더 접수한다
center.add_complaint("이윤수", "yoonsoo@codeit.kr", "에어컨이 안 들어와요...")
center.add_complaint("손동욱", "dongwook@codeit.us", "결제가 제대로 안 되는 거 같군요")
center.add_complaint("김현승", "hyunseung@codeit.ca", "방을 교체해주세요")

# 문의를 처리한다
center.process_complaint()
center.process_complaint()

# 스택 리뷰
print("stack 리뷰\n")


def parentheses_checker(string):
    """주어진 문자열에 괄호가 있는지 파악하는 메소드"""
    print("테스트 하는 문자열 : {}".format(string))
    stack = deque()
    string1 = list(string)
    for i in range(len(string1)):
        if string1[i] == "(":
            stack.append(i)
        elif string1[i] == ")":
            if stack:
                stack.pop()
            else:
                print("문자열 {} 번째 위치에 있는 닫는 괄호에 맞는 열리는 괄호가 없습니다".format(i))
    for i in reversed(range(len(stack))):
        print("문자열 {} 번째 위치에 있는 괄호가 닫히지 않았습니다".format(stack[i]))

case1 = "(1+2)*(3+5)"
case2 = "((3*12)/(41-31))"
case3 = "((1+4)-(3*12)/3"
case4 = "(12-3)*(56/3))"
case5 = ")1+14)/3"
case6 = "(3+15(*3"

parentheses_checker(case1)
parentheses_checker(case2)
parentheses_checker(case3)
parentheses_checker(case4)
parentheses_checker(case5)
parentheses_checker(case6)







queue = deque() # 추상자료형 queue에 대해서...

queue.append("첫째")  # 큐는 선입선출이기 때문에 앞의것을 먼저 삭제하고 삽입은 항상 뒤에서만 가능
queue.append("둘째")
queue.append("셋째")
queue.append("넷째")
queue.append("다섯째")

print(queue)

queue.popleft()
print(queue)

