# Создать телефонный справочник с возможностью импорта и экспорта данных в формате 
# .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться 
# в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска 
# определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.

def enter_first_name():
    return input("Введите имя абонента: ").title()

def enter_second_name():
    return input("Введите фамилию абонента: ").title()

def enter_family_name():
    return input("Введите отчество абонента: ").title()

def enter_phone_number():
    return input("Введите номер телефона: ")

def enter_address_number():
    return input("Введите адрес абонента: ").title()

def enter_data():
    name = enter_first_name()
    surname = enter_second_name()
    family = enter_family_name()
    number = enter_phone_number()
    address = enter_address_number()
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(f'{name} {surname} {family}\n{number}\n{address}\n\n')

def print_data():
    with open('book.txt', 'r', encoding='utf-8') as file:
        print(file.read())


def change_contact():
    name_to_change = input("Введите имя или фамилию контакта для изменения: ").title()
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')
    
    found = False
    updated_contacts = []
    
    for item in data:
        new_item = item.replace('\n', ' ').split()
        if name_to_change in new_item[:2]: 
            found = True
            print("Найден контакт для изменения:")
            print(item)
            new_name = input("Введите новое имя: ").title()
            new_surname = input("Введите новую фамилию: ").title()
            new_family = input("Введите новое отчество: ").title()
            new_number = input("Введите новый номер телефона: ")
            new_address = input("Введите новый адрес: ").title()
            updated_contact = f'{new_name} {new_surname} {new_family}\n{new_number}\n{new_address}\n'
            updated_contacts.append(updated_contact)
        else:
            updated_contacts.append(item)

    if found:
        with open('book.txt', 'w', encoding='utf-8') as file:
            file.write('\n\n'.join(updated_contacts))
        print("Контакт успешно обновлен.")
    else:
        print("Контакт не найден.")

def delete_contact():
    name_to_delete = input("Введите имя или фамилию контакта для удаления: ").title()
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')
    
    found = False
    updated_contacts = []
    
    for item in data:
        new_item = item.replace('\n', ' ').split()
        if name_to_delete in new_item[:2]: 
            found = True
            print("Контакт для удаления найден:")
            print(item)
        else:
            updated_contacts.append(item)

    if found:
        with open('book.txt', 'w', encoding='utf-8') as file:
            file.write('\n\n'.join(updated_contacts))
        print("Контакт успешно удален.")
    else:
        print("Контакт не найден.")


def search_line():
    print('Выберите вариант поиска:\n'
          '1. Имя\n'
          '2. Фамилия\n'
          '3. Отчество\n'
          '4. Телефон\n'
          '5. Адрес\n')
    index = int(input('Введите вариант: ')) - 1
    if index < 0 or index > 6:
        print("Некорректный вариант.")
        return
    
    if index == 5:
        change_contact()
    elif index == 6:
        delete_contact()
    else:
        searched = input('Введите поисковые данные: ').title()
        with open('book.txt', 'r', encoding='utf-8') as file:
            data = file.read().strip().split('\n\n')
            for item in data:
                new_item = item.replace('\n', ' ').split()
                if searched in new_item[index]:
                    print(item, end="\n\n")


def interface():
    cmd = 0
    while cmd != '4':
        print("Выберите действие: \n"
              "1. Добавить контакт\n"
              "2. Вывести все контакты\n"
              "3. Поиск контакта\n"
              "4. Изменить контакт\n"
              "5. Удалить контакт\n"
              "6. Выход\n")
        cmd = input("Введите действие: ")
        while cmd not in ('1', '2', '3', '4', '5', '6'):
            print('Некорректный ввод')
            cmd = input("Введите действие: ")
        match cmd:
            case '1':
                enter_data()
            case '2':
                print_data()
            case '3':
                search_line()
            case '4':
                change_contact()
            case '5':
                delete_contact()
            case '6':
                print('Всего доброго! ')
            

interface()