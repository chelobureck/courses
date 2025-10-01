#  Логический тип данных. Операторы: условные, сравнения, логические 
# Logical data type. Operators: conditional, comparison, logical


# Ответ в зависимости от дня суток
# Answer depending on the day of day
def time_of_day():

    time = input("введите время суток:").lower()  # enter time of day

    if time == "утро" or time == "morning":  
        print("доброе утро")  # good morning
    elif time == "день" or time == "day":
        print("добрый день")  # good afternoon
    elif time == "вечер" or time == "evening":
        print("добрый вечер")  # good evening
    else:
        print("здравствуйте. (точное время не известно)")  
        # hello (exact time not known)


# Проверка региона машины по номеру
# Checking the region of the car by number
def region_num_car():

    region_num = input("Введите номер региона:")  # enter region number

    if region_num == "01":
        print("Этот номер региона города Бишкек")  
        # This region number belongs to Bishkek city
    elif region_num == "02":
        print("Этот номер региона город Ош")  
        # This region number belongs to Osh city
    elif region_num == "03":
        print("Этот номер региона Баткенской области")  
        # This region number belongs to Batken region
    elif region_num == "04":
        print("Этот номер региона Джалал-Абадской области")  
        # This region number belongs to Jalal-Abad region
    elif region_num == "05":
        print("Этот номер региона Нарынской области")  
        # This region number belongs to Naryn region
    elif region_num == "06":
        print("Этот номер региона Ошской области")  
        # This region number belongs to Osh region
    elif region_num == "07":
        print("Этот номер региона Таласской области")  
        # This region number belongs to Talas region
    elif region_num == "08":
        print("Этот номер региона Чуйской области")  
        # This region number belongs to Chuy region
    elif region_num == "09":
        print("Этот номер региона Иссык-Кульской области")  
        # This region number belongs to Issyk-Kul region
    elif region_num == "10":
        print("Этот номер иностранного региона")  
        # This region number belongs to a foreign region
    else:
        print(f"Неверный регион: {region_num}. (номера регионов от 01 до 10):")  
        # Invalid region (region numbers are from 01 to 10)


# Комментарий по температуре на улице в градусах цельсия
# Comment on the outside temperature in degrees Celsius
def chek_temp():

    temp = int(input("Введите температуру в градусах: "))  
    # enter temperature in degrees

    if -30 < temp <= 5:
        print("холодно")  # cold
    elif 5 < temp <= 15:
        print("прохладно")  # cool
    elif 15 < temp <= 25:
        print("тепло")  # warm
    elif 25 < temp <= 40:
        print("жарко")  # hot
    else:
        print("несовместимая с жизнью температура!")  
        # incompatible with life temperature
