from validate_docbr import CPF

class Cpf:
    def __init__(self, cpf):
        self.__cpf = self.__doc_sanitization(cpf)

        if((not self.valid_doc()) or (not self.__cpf)):
            raise ValueError("Invalid CPF value!")

    def __str__(self):
        return self.__format_doc()

    def __format_doc(self):
        cpf_mask = CPF()
        return cpf_mask.mask(self.__cpf)

    def __doc_sanitization(self, cpf):
        if(type(cpf) == str):
            return cpf.strip()
        else:
            return ""

    def valid_doc(self):
        cpf = CPF()

        return cpf.validate(self.__cpf)