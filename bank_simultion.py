from random import randint
from datetime import datetime
class Basic:

    def __init__(self, name, password=None):
        self.name = name
        self.__password = password
        self._Id = int(randint(11, 99) / 333 * 100000)
        self.cash_result = 0

    def __str__(self):
        return f"{self.name} Welcome"

    def signin(self, user_name, user_password):
        if self.name == user_name and self.__password == user_password:
            return f"{self.name}, {self.__password}"
        else:
            return "User Dont Found"

    @property
    def my_name(self):
        return f"{self.name} {self.__password}"

    @my_name.setter
    def my_name(self, sinfo):
        name, password = sinfo.split(",")
        self.name = name
        self.__password = password

    @my_name.deleter
    def my_name(self):
        self.name = None
        self.__password = None

    def pass_info(self):
        return self.__password


class Customer(Basic):
    def __init__(self, name, password):
        super().__init__(name, password)
        self._Id = int(randint(11, 99) / 333 * 100000)
        self.cash_result = 0

    @staticmethod
    def last_time():
        return datetime.now().ctime()
    def cash_give(self, cash):
        self.cash_result += cash

        return f"{self.name} money:{self.cash_result} "


class Boss(Basic):
    def __init__(self, name, password, departmant=None):
        super().__init__(name, password)

        self.departmant = departmant

    def in_departmant(self):
        for i in self.departmant:
            print(i.name + "   " + i.pass_info())

    def all_money_in_bank(self):
        total = 0
        for i in self.departmant:
            total += i.cash_result
        return total


customer1 = Customer("mehmet", "131425")
customer2 = Customer("sinan", "fet4785")

# print(customer1.my_name)
# print(customer2.my_name)
# customer1.my_name="mehmet,147iea"
# print(customer1.my_name)

boss1 = Boss("mehmetali", "7865icvö", [customer1, customer2])
print(boss1.in_departmant())

# print(customer1.cash_result)
# customer1.cash_give(87)
# print(customer1.cash_result)

print(customer1.cash_give(-80))
print(customer2.cash_give(90))
print(boss1.all_money_in_bank())
