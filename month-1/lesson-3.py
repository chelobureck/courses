#  Операторы: принадлежности, назначения. Циклы;
# Operators: belongings, assignments. Cycles;



# цикл for
# word = "KYRGYZSTAN"
# for letter  in word:
#     if letter == "S":
#         break
#     if letter in "YRZ":
#         continue
#     print(letter)

sum_total = 100
percent = 0.1
years = 10
for year in range(1, years+1):
    sum_total += sum_total * percent
    print(f"{year}) {round(sum_total, 2)}")


# цикл while
# counter = 0
# while counter != 50:
#     counter += 1
#     if counter == 25:
#         break
#     if counter in range(16, 19+1):
#         continue
#     print("hello", counter)



# оператор назначения
# number = 5
# number += 3
# number **= 2
# number //= 2
# print(number)



# оператор принадлежности in
# print(2 in range(1, 11))
# print(10 in range(1, 11))

# word = "geeks"
# print("q" in word)
# print("g" in word)


# рефакторинг кода
# counter = 7

# while counter > 0:
#     time = input(f"введите время суток({counter}):").lower()  # enter time of day
    
#     if time == "stop":
#         print("exit...")
#         break
#     if time == "утро" or time == "morning":  
#         print("доброе утро")  # good morning
#     elif time == "день" or time == "day":
#         print("добрый день")  # good afternoon
#     elif time == "вечер" or time == "evening":
#         print("добрый вечер")  # good evening
#     else:
#         print("здравствуйте. (точное время не известно)")
#     counter -= 1