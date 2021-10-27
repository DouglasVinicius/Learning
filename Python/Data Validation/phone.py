import re

class Phone_br:
    def __init__(self, phone):
        self.phone = phone

        if(not self.validation()):
            raise ValueError("Invalid brazilian phone number!")

    def __format(self):
        expression = ("(55)?([0-9]{2})?([0-9]{4,5})([0-9]{4})")
        match_phone = re.findall(expression, self.phone)

        return f"+55 ({match_phone[0][1]}) {match_phone[0][2]}-{match_phone[0][3]}"

    def __str__(self):
        return self.__format()

    def validation(self):
        expression = re.compile("([0-9]{2})?[0-9]{10,11}")
        match_phone = expression.match(self.phone)

        return match_phone