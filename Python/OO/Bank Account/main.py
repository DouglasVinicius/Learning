from client import Client
from bank_account import Account

MIN_DEP = 300

def new_client(current_number):
    name = input("Name: ")
    salary = int(input("Salary: "))
    number = current_number
    password = input("Password: ")
    banks = Account.codigos_bancos()

    while(True):
        valid = False
        print("Banks")
        for bank, code in enumerate(banks):
            print(f"{bank}: {code}", end=", ")

        bank_code = int(input("\nBank code: "))
        for bank2, code2 in enumerate(banks):
            if(bank_code == bank2):
                valid = True
                break

        if(valid):
            break
        else:
            print("Invalid bank code!")


    while(True):
        initial_deposit = int(input(f"Initial deposit (minimum = {MIN_DEP}): "))
        if(initial_deposit < MIN_DEP):
            print("Inválid value!")
        else:
            break

    return Client(name, salary, number, password, bank_code, initial_deposit)

def operations(clients_list, choice):
    client = input("Client: ").title()

    for cl in clients_list:
        if cl == client:
            if(choice == 2):
                print(cl.__str__())
            else:
                value = int(input("Value: "))
                if(choice == 3):
                    cl.account.deposit(value)
                else:
                    password = input("Password: ")
                    if(choice == 4):
                        cl.account.withdraw(value, password)
                    elif(choice == 5):
                        dest_client = input("Destination client: ").title()
                        index_dest = clients_list.index(dest_client)
                        if(index_dest != -1):
                            cl.account.transfer(clients_list[index_dest].account, value, password)
                        else:
                            print("Invalid destination client!")
            return

    print("Invalid client!")

def main():
    clients = []
    choice = 0
    current_number = 0

    while(True):
        choice = int(input("(1)New client   (2)Balance   (3)Deposit   (4)Withdraw   (5)Transfer   (Other)Exit"))
        if(choice == 1):
            current_number += 1
            clients.append(new_client(current_number))
        elif((choice > 1) and (choice < 6)):
            operations(clients, choice)
        else:
            print("Thank you for use this aplication!")
            break

if __name__ == "__main__":
    main()