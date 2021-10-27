from cpf import Cpf
from cnpj import Cnpj

class Doc:
    @staticmethod
    def doc_choice(doc):
        if(len(doc) == 11):
            return Cpf(doc)
        elif(len(doc) == 14):
            return Cnpj(doc)
        else:
            raise IOError("Invalid quantity of characters!")