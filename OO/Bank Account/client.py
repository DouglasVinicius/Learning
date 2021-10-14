from bank_account import Account

class Client:
    def __init__(self, name, salary, number, password, bank_code, initial_deposit):
        self.__name = name.title()
        self.salary = salary
        self.account = Account(number, name, initial_deposit, salary*2, password, bank_code)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def __str__(self):
        return self.account

    def __eq__(self, account):
        return self.name == account