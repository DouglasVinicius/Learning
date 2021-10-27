from validate_docbr import CNPJ

class Cnpj:
    def __init__(self, cnpj):
        self.__cnpj = self.__doc_sanitization(cnpj)

        if((not self.valid_doc()) or (not self.__cnpj)):
            raise ValueError("Invalid cnpj value!")

    def __str__(self):
        return self.__format_doc()

    def __format_doc(self):
        cnpj_mask = CNPJ()
        return cnpj_mask.mask(self.__cnpj)

    def __doc_sanitization(self, cnpj):
        if(type(cnpj) == str):
            return cnpj.strip()
        else:
            return ""

    def valid_doc(self):
        cnpj = CNPJ()

        return cnpj.validate(self.__cnpj)