import random

def guess_number(user_num: int) -> int | None:
    """
    функция угадывает число от 1 до 100 за минимальное количество попыток
    функция принимает число от пользователя и пытается угадать число
    возвращает угаданное число или ничего, если пользователь ввел exit или ошибку
    """
    
    if not 1 <= user_num <= 100:
        print("введите число от 1 до 100")
        return None

    low = 1
    high =  100
    attempts = 0
    guesses = []

    while True:
        
        rundom_num = random.randint(low, high) 
        """ 
        rundom_num = (low + high) // 2 (это второй вариант поиска,
        более стабильный и лучше, но я использовал рандом чтобы практиовать работу с библиотеками)
        """
        attempts += 1
        guesses.append(rundom_num)

        if rundom_num == user_num:
            print(f"угадано за {attempts} попыток")

            with open("results.txt", "a",) as file:
                file.write(f"Загаданное число: {user_num}\n")
                file.write(f"Количество попыток: {attempts}\n")
                file.write(f"Список попыток: {guesses}\n")

            return rundom_num

        user_response = input(f"ваше число {rundom_num}? напшиите 'больше', 'меньше' или 'да' (exit - выход): ").lower()
        
        if user_response == "exit":
            print("выход из программы")
            return None
        
        if user_response == "больше":
            low = rundom_num + 1
        elif user_response == "меньше":
            high = rundom_num - 1
        elif user_response == "да":
            print(f"угадано за {attempts} попыток")
            return rundom_num
        else:
            print("ошибка, введите только 'больше', 'меньше' или 'да'")
            continue


while True:
    
    user_res = input("загадайте число от 1 до 100 (exit - выход из программы): ")
    if user_res.lower() == "exit":
        print("выход из программы")
        break

    try:
        user_num = int(user_res)
    except ValueError:
        print("введите число без точки")
        continue

    result = guess_number(user_num)
    if result is not None:
        print(f"ваше число {result}")
        break