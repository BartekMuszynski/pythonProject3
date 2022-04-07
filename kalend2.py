import calendar
from calendar import monthrange
from datetime import datetime, date
def date_check2():
    inputdate = input("Podaj date w formacie 'dd/mm/yyyy' : ")
    y = inputdate.split('/')
    if len(y) == 1:
        year = int(y[-1])
        if calendar.isleap(year) == True:
            x = print("Rok ktory podales jest przestepny")
        else:
            x = print("Rok ktory podales nie jest przestepny ")
        return (x)
    elif len(y) == 2:
        year = int(y[-1])
        month = int(y[-2])
        if calendar.isleap(year) == True:
            x = print("Rok ktory podales jest przestepny")
        else:
            x = print("Rok ktory podales nie jest przestepny ")
        y = monthrange(year, month)
        x1 = print("Miesiac ktory podales ma ", y[-1], "dni")
        return (x, x1)
    elif len(y) == 3:
        year = int(y[-1])
        month = int(y[-2])
        day = int(y[0])
        if calendar.isleap(year) == True:
            x = print("Rok ktory podales jest przestepny")
        else:
            x = print("Rok ktory podales nie jest przestepny ")
        y = monthrange(year, month)
        x1 = print("Miesiac ktory podales ma ", y[-1], "dni")
        day_of_year = date(year, month, day).timetuple().tm_yday
        x3 = print("Dzien roku: ", day_of_year)
        return (x, x1, x3)

date_check2()