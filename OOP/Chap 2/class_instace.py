class User:
    count = 0
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        User.count += 1

    def __str__(self):
        return "사용자 : {}, 이메일 : {}, 비밀번호 : *****".format(self.name, self.email)

    def say_hello(self):
        print("안녕하세요 저는 {}입니다".format(self.name))

    def login(self, my_email, my_password):
        if self.email == my_email and self.password == my_password:
            print("로그인 성공")
        else:
            print("로그인 실패")

    def check_name(self, name):
        return self.name == name

    @classmethod
    def number_of_users(cls):
        print("총 유저 수는 {} 명 입니다".format(cls.count))


user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Yongjin", "choyj1085@naver.com", "12345")
user4 = User("JOE", "choyj1085@gmail.com", "1234")
# 같은 class but 서로 다른 instace


condition = True
condition_string = "nice" if condition else "not nice"
print(condition_string)


User.say_hello(user1)   #class에서 method를 호출
user1.say_hello()   #instance에 method를 호출. instance가 자동으로 parameter로 호출됨
user1.login("choyj1085@naver.com", "1234")
print(user1.check_name("조용진"))

User.number_of_users()
user1.number_of_users()

