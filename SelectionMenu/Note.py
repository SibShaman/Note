# Заметка должна содержать идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения
# заметки
from datetime import datetime


class Note:
    my_list = []

    def __init__(self, my_list):
        self.my_list = my_list

    @staticmethod
    def create_entry(my_list):
        count = 0
        if len(my_list) > 0:
            for elem in range(len(my_list)):
                temp_count = my_list[elem]
                count = temp_count['id']

        new_entry = {'id': '', 'title': '', 'description': '', 'date': ''}
        add_list = []
        new_entry['id'] = int(count) + 1
        new_entry['title'] = input('Введите заголовок: \n')
        new_entry['description'] = input('Введите текст заметки: \n')
        new_entry['date'] = datetime.now()
        add_list.append(new_entry)
        return add_list

    @staticmethod
    def change_entry(my_list):
        text = input('Введите id заметки или заголовок: ')
        find_el = [x for x in my_list if (x['id'] == text or x['title'] == text)]
        for i in range(len(my_list)):
            if my_list[i]['id'] == find_el[0]['id']:
                my_list[i]['title'] = input('Введите заголовок: \n')
                my_list[i]['description'] = input('Введите текст заметки: \n')
                my_list[i]['date'] = datetime.now()
        return my_list

    @staticmethod
    def find_entry(my_list):
        text = input('Введите id заметки или заголовок: ')
        print([x if (x['id'] == text or x['title'] == text) else 'not found' for x in my_list])

    @staticmethod
    def delete_entry(my_list):
        text = input('Введите id заметки или заголовок: ')
        find_el = [x for x in my_list if (x['id'] == text or x['title'] == text)]
        for i in range(len(my_list)):
            if my_list[i]['id'] == find_el[0]['id']:
                del my_list[i]
                break
        return my_list

    @staticmethod
    def save_entry(my_list):
        pass

    @staticmethod
    def show_entry(my_list):
        pass
