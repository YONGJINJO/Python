class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return "사용자 : {}, 이메일 : {}, 비밀번호 : *****".format(self.name, self.email)


user1 = User("Young", "young@codeit.kr", "123456")

user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

print(user1)
