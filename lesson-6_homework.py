

def password_check(password: str) -> bool:
    """принимает пароль в виде строки и проверяет ее на безопасность. возвращает True если с безопасностью проблем нет.
    возвращает False если программа посчитает ее не безопасной/простой."""
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~"

    if len(password) > 5:
        
        check_password = [
            any(elem in lowercase for elem in password),
            any(elem in uppercase for elem in password),
            any(elem in digits for elem in password),
            any(elem in symbols for elem in password)
        ]

        if all(check_password):
            return True
        else:
            return False
        
    else:
        return False

def nearest_number(numbers: list[int | float] | tuple[int | float], target_number: int | float = 0) -> int | float:
    """функция принимает список/кортеж и целевое число (по умолчанию = 0). возвращает число из списка/кортежа, которое ближе всего
    к целевому числу."""
    db_num = []
    for num in numbers:
        db_num.append(abs(target_number - num))
    res = db_num.index(min(db_num))
    return numbers[res]