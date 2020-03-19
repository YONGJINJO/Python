class Cashier:
    company_name = "Apple"
    raise_percentage = 1.03
    phone_price = 4000

    def __init__(self, name, wage, number_sold = 0):
        self.name = name
        self.wage = wage
        self.number_sold = number_sold

    def raise_pay(self):
        self.wage *= self.raise_percentage

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

jiwoon = Cashier("jiwwon", 8900, 0)
jiwoon.raise_pay()
print(jiwoon.wage)

print(jiwoon.take_order(7000))
print(jiwoon.take_order(3000))

print(jiwoon.phone_price)
print(Cashier.phone_price)

print(jiwoon.number_sold)
print(jiwoon)