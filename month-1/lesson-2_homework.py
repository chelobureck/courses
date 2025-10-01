# Программа для определения знака зодиака  
# Program to determine zodiac sign

month = int(input("Введите месяц рождения: "))  # Enter birth month

# Проверка на сущесвтование месяца  
# Check if month exists
if 0 < month < 13:

    day = int(input("Введите день рождения: "))  # Enter birth day

    # Январь  
    # January
    if month == 1:
        if 21 <= day <= 31:
            print("Водолей")  # Aquarius
        elif 1 <= day <= 20:
            print("Козерог")  # Capricorn
        else:
            print("Неправильный день (учтите что Январь длится от 1 до 31 числа).")  
            # Invalid day (note: January lasts from 1 to 31)

    # Февраль  
    # February
    elif month == 2:
        if 20 <= day <= 28:
            print("Рыбы")  # Pisces
        elif 1 <= day <= 19:
            print("Водолей")  # Aquarius
        else:
            print("Неправильный день (учтите что Февраль длится от 1 до 28 числа, если вы родились в високосном году то введите 28 число).")  
            # Invalid day (note: February lasts from 1 to 28, enter 28 if born in a leap year)

    # Март  
    # March
    elif month == 3:
        if 21 <= day <= 31:
            print("Овен")  # Aries
        elif 1 <= day <= 20:
            print("Рыбы")  # Pisces
        else:
            print("Неправильный день (учтите что Март длится от 1 до 31 числа).")  
            # Invalid day (note: March lasts from 1 to 31)

    # Апрель  
    # April
    elif month == 4:
        if 21 <= day <= 30:
            print("Телец")  # Taurus
        elif 1 <= day <= 20:
            print("Овен")  # Aries
        else:
            print("Неправильный день (учтите что Апрель длится от 1 до 30 числа).")  
            # Invalid day (note: April lasts from 1 to 30)

    # Май  
    # May
    elif month == 5:
        if 22 <= day <= 31:
            print("Близнецы")  # Gemini
        elif 1 <= day <= 21:
            print("Телец")  # Taurus
        else:
            print("Неправильный день (учтите что Май длится от 1 до 31 числа).")  
            # Invalid day (note: May lasts from 1 to 31)

    # Июнь  
    # June
    elif month == 6:
        if 22 <= day <= 30:
            print("Рак")  # Cancer
        elif 1 <= day <= 21:
            print("Близнецы")  # Gemini
        else:
            print("Неправильный день (учтите что Июнь длится от 1 до 30 числа).")  
            # Invalid day (note: June lasts from 1 to 30)

    # Июль  
    # July
    elif month == 7:
        if 23 <= day <= 31:
            print("Лев")  # Leo
        elif 1 <= day <= 22:
            print("Рак")  # Cancer
        else:
            print("Неправильный день (учтите что Июль длится от 1 до 31 числа).")  
            # Invalid day (note: July lasts from 1 to 31)

    # Август  
    # August
    elif month == 8:
        if 22 <= day <= 31:
            print("Дева")  # Virgo
        elif 1 <= day <= 21:
            print("Лев")  # Leo
        else:
            print("Неправильный день (учтите что Август длится от 1 до 31 числа).")  
            # Invalid day (note: August lasts from 1 to 31)

    # Сентябрь  
    # September
    elif month == 9:
        if 24 <= day <= 30:
            print("Весы")  # Libra
        elif 1 <= day <= 23:
            print("Дева")  # Virgo
        else:
            print("Неправильный день (учтите что Сентябрь длится от 1 до 30 числа).")  
            # Invalid day (note: September lasts from 1 to 30)

    # Октябрь  
    # October
    elif month == 10:
        if 24 <= day <= 31:
            print("Скорпион")  # Scorpio
        elif 1 <= day <= 23:
            print("Весы")  # Libra
        else:
            print("Неправильный день (учтите что Октябрь длится от 1 до 31 числа).")  
            # Invalid day (note: October lasts from 1 to 31)

    # Ноябрь  
    # November
    elif month == 11:
        if 23 <= day <= 30:
            print("Стрелец")  # Sagittarius
        elif 1 <= day <= 22:
            print("Скорпион")  # Scorpio
        else:
            print("Неправильный день (учтите что Ноябрь длится от 1 до 30 числа).")  
            # Invalid day (note: November lasts from 1 to 30)

    # Декабрь  
    # December
    elif month == 12:
        if 23 <= day <= 31:
            print("Козерог")  # Capricorn
        elif 1 <= day <= 22:
            print("Стрелец")  # Sagittarius
        else:
            print("Неправильный день (учтите что Декабрь длится от 1 до 31 числа).")  
            # Invalid day (note: December lasts from 1 to 31)

else:
    print("Вы ввели неправильный месяц (введите число от 1 до 12).")  
    # Invalid month entered (enter a number from 1 to 12)
