# Словари, множества. Устный опрос, промежуточный тест, самостоятельная работа;

color = input("Введите цвет светофора (выход - завершит работу программы): ").lower()

while color != "выход":
    if color == "красный":
        print("стой")
    elif color == "желтый":
        print("жди")
    elif color == "зеленый":
        print("иди")
    else:
        print('приграмма не принимает ничего кроме цветов светофора и "выход".')
    
    color = input("Введите цвет светофора (выход - завершит работу программы): ").lower()

print("программа завершена")



days = 1

day = int(input(f"Введите расходы за {days} день: "))

expenses = []

while days < 7:
    expenses.append(day)
    
    days += 1

    day = int(input(f"Введите расходы за {days} день: "))

expenses.append(day)
sum_expenses = sum(expenses)
med_expenses = round(sum_expenses / 7, 2)

print("программа посчитала расходы за 7 дней")
print(f"общие расходы: {sum_expenses}")
print(f"средние расходы {med_expenses}")
