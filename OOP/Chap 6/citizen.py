class Citizen:
    """주민 클래스"""
    dringking_age = 19

    def __init__(self, name, age, resident_id):
        """이름, 나이, 주민등록번호"""
        self.name = name
        self.set_age(age)
        self._resident_id = resident_id

    def authenticate(self, id_field):
        """본인 확인"""
        return self._resident_id == id_field

    def can_drink(self):
        """음주 나이 확인"""
        return self._age >= Citizen.dringking_age

    def __str__(self):
        """주민 정보 리턴"""
        return self.name + "씨는 " + str(self._age) +"살입니다!"

    def get_age(self):
        return self._age

    def set_age(self, value):
        if value < 0:
            print("나이는 0보다 작을 수 없습니다.")
            self._age = 0
        else:
            self._age = value

    @property
    def age(self):
        print("나이를 리턴합니다")
        return self._age

    @age.setter
    def age(self, value):
        print("나이를 설정합니다")
        if value < 0:
            print("나이는 0보다 작을 수 없습니다.")
            self._age = 0
        else:
            self._age = value



kyusik = Citizen("최규식", 25, "12345678")
young = Citizen("young", -10, "12345679")

young.set_age(-10)

print(young._age)