class Employee:
    company_name = "Apple"
    raise_percentage = 1.03

    def __init__(self, name, wage):
        self.name = name
        self.wage = wage

    def raise_pay(self):
        self.wage *= self.raise_percentage

    def __str__(self):
        return Employee.company_name + " 직원: " + self.name

class Cashier(Employee):

    raise_percentage = 1.05
    phone_price = 4000

    def __init__(self, name, wage, number_sold):
        super().__init__(name, wage) #super 는 자식class 에서 부모 class의 method 호출 시 사용, self 사용 안해도됨
        self.number_sold = number_sold

    def take_order(self, money_received):
        if Cashier.phone_price > money_received:
            print("돈이 충분하지 않습니다")
            return money_received
        else:
            self.number_sold += 1
            change = money_received - Cashier.phone_price
            return change

    def __str__(self):
        return Cashier.company_name + " 계산대 직원: " + self.name

class Delievery(Employee):
    pass



jiwoon = Cashier("jiwoon", 8900, 0)
jiwoon.raise_pay()

sunghyun = Delievery("sunghyun", 10000)
print(jiwoon.wage)
print(jiwoon)
print(sunghyun)

print(Cashier.mro())
print(list.mro())
print(isinstance(jiwoon, Cashier))
print(isinstance(jiwoon, Delievery))
print(isinstance(jiwoon, Employee))

print(issubclass(Cashier, object))
print(issubclass(Cashier, Employee))
print(issubclass(Cashier, Delievery))