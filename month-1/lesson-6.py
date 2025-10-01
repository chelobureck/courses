# Урок 6. Функции: виды параметров, возвращение данных, виды аргументов;

"""как создаются функции"""
"""
определение наименования(параметры):
    тело функции (логика)
    возвращение обьекта (рещультат)

наименования(аргументы)
"""

def func_name(name: str, username: str = "неизвестно") -> str:
    """принимает имя и фамилие, возвращает текст с подписанными данными"""
    return f"name: {name} username: {username}"

#data = func_name("max", "verstappen")
#print(data)
#print(help(func_name))


def year_birthey(name: str, age: int) -> str:
    """принимает имя и возраст и возвращает имя с загдавной букфы и год рождения"""
    real_year = 2025
    #data_name = name.title()
    #data_age = real_year - age
    if type(age) == int and type(name) == str:
        if 0 < age < 120:
            return f"{name.title()}, год рождения: {real_year - age}"
        else:
            return "такого возраста нет"
    elif type(age) != int:
        return "вместо возраста было введено слово (проверьте тип данных)"
    else:
        return "вместо имени было введено число (проверьте тип данных)"

data = year_birthey("azamаt", 25) 
print(data)
#print(help(year_birthey))

data = year_birthey("azamаt", "adc")
print(data)

data = year_birthey(25, 25)
print(data)

data = year_birthey("bermet", 12)
print(data)