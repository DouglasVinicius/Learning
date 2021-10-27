MAX_ATTEMPS = 3
TRANSFER_TARIFF = 5.0

class Account:
    def __init__(self, number, owner, balance, transfer_limit, password, bank_code):
        self.__number = number
        self.__owner = owner
        self.__balance = balance
        self.__transfer_limit = transfer_limit
        self.__password = password
        self.__max_attemps = MAX_ATTEMPS
        self.__block_account = False
        self.__transfer_tariff = TRANSFER_TARIFF
        self.bank_code = bank_code

    @property
    def number(self):
        return self.__number

    @property
    def owner(self):
        return self.__owner.title()

    @property
    def balance(self):
        return self.__balance

    @property
    def transfer_limit(self):
        return self.__transfer_limit

    @property
    def block_account(self):
        return self.__block_account

    @transfer_limit.setter
    def transfer_limit(self, transfer_limit):
        self.__transfer_limit = transfer_limit

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Itau': '184', 'Caixa': '104', 'Bradesco': '237', 'NU': '260', 'Sicredi': '748', 'Banrisul': '41'}

    def deposit(self, value):
        if(not self.block_account):
            self.__balance += value
            return True
        else:
            print("Your account is blocked!")
            return False

    def __have_balance(self, value, transfer, bank_code):
        different_bank = (bank_code != None)
        if(transfer and different_bank):
            final_value = value + self.__transfer_tariff
            return self.__balance >= final_value
        else:
            return self.__balance >= value

    def __have_limit(self, value):
        return value <= self.__transfer_limit

    def __successful_withdrawal(self, value, transfer, bank_code):
        different_bank = (bank_code != None)
        if(transfer and different_bank):
            self.__balance -= (value + self.__transfer_tariff)
            print("Transfer successful!")
        else:
            self.__balance -= value
            print("Withdrawal successful!")

        self.__max_attemps = MAX_ATTEMPS
    
    def withdraw(self, value, password, transfer = False, bank = None):
        if(not self.block_account):
            if(self.__password == password):
                if(self.__have_balance(value, transfer, bank)):
                    if(self.__have_limit(value)):
                        self.__successful_withdrawal(value, transfer, bank)
                        return True
                    else:
                        print("Error, you exceeded your account limit of transfer per day!")
                else:
                    print("Error, you don't have this balance in your account!")
            else:
                self.__max_attemps -= 1
                if(not self.verify_block()):
                    print("Incorrect password, you still have {} attemps before your account to lock!".format(self.__max_attemps))
        else:
            print("Your account is blocked!")
            return False

    def __str__(self):
        return ("Account number: {}\nOwner: {}\nBalance: ${}\nTransfer_limit (per day): {}\n".format(self.__number, self.__owner.title(), self.__balance, self.__transfer_limit))

    def __eq__(self, conta):
        return (self.number == conta.number) and (self.owner == conta.owner)

    def transfer(self, receiver, value, password):
        if(self.withdraw(value, password, True, receiver.bank_code)):
            receiver.deposit(value)
            return True
        return False

    def verify_block(self):
        if(self.__max_attemps <= 0 and self.__block_account == False):
            print("Your account has been blocked!")
            self.__block_account = True
            
        return self.__block_account