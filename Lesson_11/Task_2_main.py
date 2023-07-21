import json
import sys
import os
name_dict = sys.argv[1]

def open_json(name_dict):
    if os.path.exists(name_dict):
      with open(name_dict, 'r') as book:
        book_list = json.load(book)
        return book_list
    else:
       try:
           raise FileNotFoundError
       except:
           print('File not exist')
           sys.exit()


def change_json(name_dict, book_list):
    with open(name_dict, 'w') as book:
        json.dump(book_list, book, indent=4)


def new_entries(book_list):
    first_name = input('first name is ')
    first_name = first_name.capitalize()
    last_name = input('last name is ')
    last_name = last_name.capitalize()
    telephone_number = input('telephone number is ')
    telephone_number = telephone_number.replace(' ', '')
    city = input('city is ')
    city = city.capitalize()
    state = input('state is ')
    state = state.capitalize()
    new_entry = {"first name": first_name, "last name": last_name, "telephone number": telephone_number, "city": city,
                 "state": state}
    book_list.append(new_entry)
    change_json(name_dict, book_list)
    print('Contact successfully added to file')


def first_name(book_list):
    first_name = input('first name is ')
    first_name = first_name.capitalize()
    j = len(book_list)
    for i in range(len(book_list)):
        items = book_list[i].items()
        if ('first name', first_name) in items:
            print(book_list[i])
            j = j - 1
    if j == len(book_list):
        print('There is no such contact in file')


def last_name(book_list):
    last_name = input('last name is ')
    last_name = last_name.capitalize()
    j = len(book_list)
    for i in range(len(book_list)):
        items = book_list[i].items()
        if ('last name', last_name) in items:
            print(book_list[i])
            j = j - 1
    if j == len(book_list):
        print('There is no such contact in file')


def full_name(book_list):
    first_name = input('first name is ')
    first_name = first_name.capitalize()
    last_name = input('last name is ')
    last_name = last_name.capitalize()
    j = len(book_list)
    for i in range(len(book_list)):
        items = book_list[i].items()
        if ('last name', last_name) and ('first name', first_name) in items:
            print(book_list[i])
            j = j - 1
    if j == len(book_list):
        print('There is no such contact in file')


def search_by_number(book_list):
    number = input('telephone number is ')
    number = number.replace(' ', '')
    j = len(book_list)
    for i in range(len(book_list)):
        items = book_list[i].items()
        if ('telephone number', number) in items:
            print(book_list[i])
            j = j - 1
    if j == len(book_list):
        print('There is no such contact in file')


def search_by_place(book_list):
    place = input('your location is ')
    place = place.capitalize()
    j = len(book_list)
    for i in range(len(book_list)):
        items = book_list[i].items()
        if ('city', place) in items or ('state', place) in items:
            print(book_list[i])
            j = j - 1
    if j == len(book_list):
        print('There is no such contact in file')


def delete_record(book_list):
    number = input('telephone number you want delete is ')
    number = number.replace(' ', '')
    j = 0
    for i in range(len(book_list)):
        items = book_list[i].items()
        if ('telephone number', number) in items:
            dict_for_delete=i
            j = j + 1
    if j == 0:
        print('There is no such contact in file')
    else:
        book_list.pop(dict_for_delete)
        change_json(name_dict, book_list)
        print('Contact deleted successfully')


def update_record(book_list):
    number = input('telephone number you want delete is ')
    number = number.replace(' ', '')
    j = 0
    for i in range(len(book_list)):
        items = book_list[i].items()
        if ('telephone number', number) in items:
            dict_for_delete = i
            j = j + 1
    if j == 0:
        print('There is no such contact in file')
    else:
        book_list.pop(dict_for_delete)
        change_json(name_dict, book_list)
        new_entries(book_list)
        print('Contact deleted successfully')


def your_choice(name_dict):
    f = 0
    k = 0
    while k == 0:
        book_list = open_json(name_dict)
        if f == 0:
            print('Add new entries - enter 1 \nSearch by first name - enter 2 \nSearch by last name - enter 3 \nSearch by full name - enter 4 \nSearch by telephone number - enter 5 \nSearch by city or state - enter 6 \nDelete a record for a given telephone number - enter 7 \nUpdate a record for a given telephone number - enter 8 \nExit the program - enter any other symbol')
        else:
            print('\nDo you want to take a different action?')
        choice = input('Make your choice: ')
        if choice == str(1):
            new_entries(book_list)
            f = 1
        elif choice == str(2):
            first_name(book_list)
            f = 1
        elif choice == str(3):
            last_name(book_list)
            f = 1
        elif choice == str(4):
            full_name(book_list)
            f = 1
        elif choice == str(5):
            search_by_number(book_list)
            f = 1
        elif choice == str(6):
            search_by_place(book_list)
            f = 1
        elif choice == str(7):
            delete_record(book_list)
            f = 1
        elif choice == str(8):
            update_record(book_list)
            f = 1
        else:
            print('Bye!')
            k = 1


your_choice(name_dict)
