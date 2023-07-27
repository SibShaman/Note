# Необходимо написать проект, содержащий функционал работы с заметками. Программа должна уметь создавать заметку,
# сохранять её, читать список заметок, редактировать заметку, удалять заметку.

from SelectionMenu.Note import Note
from SelectionMenu.manage import write_data, show_data, read_data

FILE_NAME = 'SelectionMenu/note.csv'


def command_menu():
    # запуск меню команд
    print('<<<<<<<<< Приложение ЗАМЕТКИ >>>>>>>>>>>>')
    print('1. Добавить запись в блокнот')
    print('2. Посмотреть список записей')
    print('3. Найти запись')
    print('4. Редактировать запись')
    print('5. Удалить запись')
    print('0. Выход')
    while True:
        in_com = input('Выберите действие: \n')
        if in_com == '1':
            read_file = read_data(FILE_NAME)      # читаем файл, если он создан, смотрим список записей для получения id
            note = Note(read_file)
            temp = note.create_entry(read_file)   # заполняем экземпляр нашими данными
            write_data(temp, FILE_NAME)           # записываем данные в файл

        elif in_com == '2':
            show_data(FILE_NAME)                  # показываем все записи в файле

        elif in_com == '3':
            read_file = read_data(FILE_NAME)  # читаем файл, если он создан, смотрим список записей для получения id
            note = Note(read_file)
            note.find_entry(read_file)

        elif in_com == '4':
            pass

        elif in_com == '5':
            pass

        elif in_com == '0':
            break

        else:
            print('Вы неправильно ввели команду')
            break
