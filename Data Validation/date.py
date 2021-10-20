from datetime import datetime, timedelta

class Date_br():
    def __init__(self):
        self.__registration_time = datetime.today()

    def __str__(self):  
        return self.__registration_time.strftime("%d/%m/%Y %H:%M:%S")

    def extend_month(self):
        month_ex = (
            "January", "February", "March",
            "April", "May", "June", "July",
            "August", "September", "October",
            "November", "December"
        )

        return f"{month_ex[self.__registration_time.month-1]}"

    def extend_week(self):
        week_ex = (
            "Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"
        )

        return f"{week_ex[self.__registration_time.weekday()-1]}"

    def recorded_time(self, pass_day=0, pass_hour=0, pass_min=0, pass_sec=0):
        return (self.__registration_time+timedelta(days=pass_day, hours=pass_hour, minutes=pass_min, seconds=pass_sec))-self.__registration_time