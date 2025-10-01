

def nearest_number(numbers: list | tuple, target_num: int) -> tuple:
    """
    функция принимает список/кортеж чисел и целевое число. 
    возвращает кортеж отсортированный по порядку близости к целевому числу
    """
    sorted_numbers = sorted(numbers, key=lambda x: abs(x - target_num))
    return target_num, sorted_numbers



def element_index(iterable: list | tuple | str = [1, 2, 3, 4, 5]):
    """
    функция принимает список/кортеж/строку(по умолчанию = [1, 2, 3, 4, 5]) и запрашивает нужный индекс.
    при идеальных условиях выводит элемент под данным индексом, а при 
    ошибке обрабатывает ее и сообщает о ней.
    """
    while True:
        user_input = input("введите индекс ('exit' - выйдет из программы):")

        if user_input.lower() == "exit":
            break

        try:
            index = int(user_input)
            print(f"элемент под индексом {index}: {iterable[index]}")
        except ValueError:
            print("введите число или 'exit': ")
        except IndexError:
            print(f"введите индекс от 0 до {len(iterable) - 1}")