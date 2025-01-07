from fileinput import filename
from typing import List

import csv
import os




# ФУНКЦИЯ НЕПОСРЕДСТВЕННОГО ФУНКЦИОНИРОВАНИЯ ПРОГРАММЫ ПРИ ПЕРВОМ ВЫБОРЕ ПОЛЬЗОВАТЕЛЯ

def global_function(action):
    from GraficUserInterface import message_first_select
    if action == "С":
        from GraficUserInterface import message_create_catalog, message_result_create_catalog
        from Business_Logic_Lower import exist_catalog, reestr_catalog
        result_exist = exist_catalog()
        name_catalog = None
        if not result_exist:
            name_catalog = message_create_catalog()
            create_catalog(name_catalog)
            reestr_catalog(name_catalog)
        return message_result_create_catalog(result_exist, name_catalog)

    elif action == "У":
        from GraficUserInterface import message_confirm_delete_catalog, message_result_delete_catalog, message_create_catalog
        from Business_Logic_Lower import exist_catalog, reestr_catalog
        if message_confirm_delete_catalog() == "Да":
            result_exist = exist_catalog()
            if result_exist:
                delete_catalog()
            return message_result_delete_catalog(result_exist)

        elif message_confirm_delete_catalog() == "Нет":
            return

    elif action == "П":
        from GraficUserInterface import message_catalogs_history
        from Business_Logic_Lower import exist_reestr
        result_exist_reestr = exist_reestr()
        if  result_exist_reestr == True:
            message_catalogs_history(f"Реестр каталогов.txt")
        else:
            print("История каталогов отсутствует, так как еще не создавалось ни одного каталога")

    elif action == "Р":
        from Business_Logic_Lower import name_catalog, exist_catalog, exist_reestr
        from GraficUserInterface import msg_offer_create_or_use_test_catalog, empty_reestr
        result_exist_ = exist_reestr()
        if  result_exist_ == False:
            select_user = empty_reestr()
            if select_user == "Т":
                work_with_catalog("test_catalog.txt")
            elif select_user == "Н":
                return
        else:
            filename = name_catalog()
            result_exist = exist_catalog()
            if result_exist:
                work_with_catalog(filename)
            else:
                result_offer = msg_offer_create_or_use_test_catalog()
                if result_offer == "Т":
                    work_with_catalog("test_catalog.txt")
                elif result_offer == "Н":
                    return



# ФУНКЦИЯ ФУНКЦИОНИРОВАНИЯ ПРОГРАММЫ ПРИ  РАБОТЕ C КАТАЛОГОМ

def work_with_catalog(path_file):
    from GraficUserInterface import msg_select_act_in_catalog
    action_in_catalog = msg_select_act_in_catalog()
    while action_in_catalog != "Н":

        if action_in_catalog == "Д":
            from GraficUserInterface import message_add_book
            name_book, author_book, year_book, genre_book = message_add_book()
            add_book(path_file, name_book, author_book, year_book, genre_book)

        elif action_in_catalog == "У":
            from GraficUserInterface import message_delete_book, view_list_books
            view_list_books(path_file)
            number_book = message_delete_book()
            delete_book(path_file, number_book)

        elif action_in_catalog == "О":
            from GraficUserInterface import view_list_books
            print(f"В текущем каталоге находятся следующие книги:  ")
            print()
            view_list_books(path_file)

        elif action_in_catalog == "П":
            from GraficUserInterface import message_search_books, print_list
            search_word = message_search_books()
            catalog = search_book(path_file, search_word)
            print_list(catalog)

        elif action_in_catalog == "С":
            from GraficUserInterface import message_sort_books, print_list
            value_sort = message_sort_books()
            sort_books = sort_catalog_main(path_file, value_sort)
            print_list(sort_books)

        elif action_in_catalog == "Э":
            from GraficUserInterface import message_result_export_catalog
            export_catalog(path_file)
            message_result_export_catalog()
        action_in_catalog = msg_select_act_in_catalog()


# ФУНКЦИИ ПРИ СОЗДАНИИ КАТАЛОГА
#___________________________________________________________________________________________________________________
# функция создания каталога и присвоения ему имени
def create_catalog(name_catalog):
    catalog = open(f"{name_catalog}.txt", "w")
    return True


# ФУНКЦИИ ПРИ УДАЛЕНИИ КАТАЛОГА
#____________________________________________________________________________________________________________________
# функция удаления каталога
def delete_catalog():
    path = os.getcwd()
    for file in os.listdir(path):
        if file.endswith(".txt"):
            os.remove(file)


# ФУНКЦИИ ПРИ РАБОТЕ В КАТАЛОГЕ
#___________________________________________________________________________________________________________________

# функция добавления книги в каталог
def add_book(file, name_book, author_book, year_book, genre_book):
    file = open(file, "a")
    file.write(f"{name_book} - {author_book} - {year_book} - {genre_book}\n")
    file.close()


# функция удаления книги из каталога
def delete_book(path_file, number_book):
    catalog = []
    file = open(path_file, "r")
    catalog = file.readlines()
    file.close()
    file = open(path_file, "w")
    for line in range(len(catalog)):
        if line != (number_book-1):
            file.write(catalog[line])
    file.close()


# функция поиска книги в каталоге
def search_book(file, search_word):
    list_search_book = []
    file = open(file, "r")
    catalog = file.readlines()
    for book in catalog:
        if search_word in book:
            list_search_book.append(book)
    file.close()
    return list_search_book


# функция сортировки книг в каталоге

def sort_catalog_main(file, value_sort):
    catalog = []
    file = open(file, "r")
    catalog = file.readlines()
    if value_sort == "Н":
        ind = 1
    elif value_sort == "А":
        ind = 0
    elif value_sort == "Г":
        ind = 2
    elif value_sort == "Ж":
        ind = 3
    sort_catalog = sorted(catalog, key= lambda line: line.split(" - ")[ind])
    file.close()
    return sort_catalog



# функция экспорта каталога
def export_catalog(file):
    catalog = []
    file = open(file, "r")
    catalog = file.readlines()

    file_csv = open("Ваш каталог книг.csv", "w", newline="")
    writer = csv.writer(file_csv)
    for line in catalog:
        writer.writerow([line])
