import requests

class Address:
    def __init__(self, cep):
        if(self.__cep_validation(cep)):
            self.cep = cep
        else:
            raise ValueError("Invalid CEP!")

    def __cep_validation(self, cep):
        if(len(cep) == 8):
            return True
        return False

    def info_with_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        req = requests.get(url)
        datas = req.json()

        return (
            datas['logradouro'],
            datas['bairro'],
            datas['localidade'],
            datas['uf']
        )

    def __str__(self):
        return f"{self.cep[0:5]}-{self.cep[5:]}"