# Урок 7. Lambda функции. Обработка исключений;

def up_first_letter(word: str) -> str:
    return word.title()

def show_words(func, words):
    for i in words:
        print(func(i))

show_words(lambda word: word.title(), ["white", "black", "red"])
show_words(len, ["car", "game", "book"])
show_words(up_first_letter, ["car", "game", "book"])


lambda_def = lambda n1, n2: n1 + n2
print(lambda_def(2, 3))
print(type(lambda_def))

countries = ["kgz", "kaz", "uzb", "tur"]
print(countries)
sorted_countries = sorted(countries, key=lambda word: word[-1])
print(sorted_countries)

filter_countries = list(filter(lambda word: word[-1] == "z", countries))
print(filter_countries)
print(help(filter))

map_countries = list(map(lambda word: word.upper(), countries))
print(map_countries)


try:
    print(2 + 9)
except:
    print("Найдена ошибка и обработана!")
else:
    print("ошибок не обнаружено")
finally:
    print("проверка завершена")
