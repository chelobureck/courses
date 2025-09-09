# счетчик букв, согласных и гласных

word = input("Введите слово(stop - остановит программу.)")
word_lower = word.lower()


# список согласных и гласных букв
vowels_ru = "аеёиоуыэюя"
consonants_ru = "бвгджзйклмнпрстфхцчшщ"
vowels_eng = "aeiou"
consonants_eng = "bcdfghjklmnpqrstvwxyz"

while word_lower != "stop":
    # Счет букв, согласных и гласных
    counter = 0
    vowels_counter = 0
    consonants_counter = 0
    
    for letter in word_lower:
        counter += 1
        if letter in vowels_ru or letter in vowels_eng:
            vowels_counter += 1
        if letter in consonants_ru or letter in consonants_eng:
            consonants_counter += 1
    
    precent_vowels = vowels_counter / counter
    precent_consonants = consonants_counter / counter

    print(f"Слово: {word}")
    print(f"Количество букв: {counter}")
    print(f"Количество гласных: {vowels_counter}")
    print(f"Количество согласных: {consonants_counter}")
    print(f"Гласные/согласные: {round(precent_vowels*100, 2)}% / {round(precent_consonants*100, 2)}%")

    word = input("Введите слово(stop - остановит программу)")
    word_lower = word.lower()