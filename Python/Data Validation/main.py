from document import Doc
from phone import Phone_br
from date import Date_br
from address import Address

def main():
    cpf = Doc.doc_choice("54136086083")        #CPF example
    cnpj = Doc.doc_choice("37186276000116")    #CNPJ example
    phone = Phone_br("5199990000")
    date = Date_br()
    addr = Address("97546550")
    
    print(cpf)
    print(cnpj)
    print(phone)
    print(date, date.extend_month(), date.extend_week(), date.recorded_time(5,5,16,51), sep="\n")
    print(addr, sep="\n")

    neighborhood, district, city, state = addr.info_with_cep()
    print(neighborhood, district, city, state, sep=", ")

if __name__ == "__main__":
    main()