# Урок 8. Контекстный менеджер “with”, работа с файлами;
# w - write (запись, перезапись)
# a - add (запись, дозапись)
# r - read (чтение файла)
from time import sleep


with open("courses/new_file.txt", "r") as file:
    for i in file.read():
        print(i)
        sleep(0.7)


# with open("courses/new_file.txt", "a") as file:
    # file.write("\nБишкек")

# file = open('courses/new_file.txt', 'w')
# file.write('Адылбеков Элдияр')
# file.close()