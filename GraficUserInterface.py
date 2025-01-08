from Business_Logic_Upper import *
from Business_Logic_Lower import *
from tabulate import tabulate


# Сообщение прветствия при запуске и завершении программы
def greeting():
    print("Добро пожаловать в приложение по управлению каталогом книг!")
    print()


def goodbye():
    print("Хорошего дня! Ждем Вас снова!")


# Вывод сообщения о  выборе первоначального действия с каталогом
def message_first_select():
    print("Пожалуйста, с помощью ввода начальных букв выберете желаемое действие: \n"
          "С - Создать каталог\n"
          "У - Удалить каталог\n"
          "П - Просмотр истории каталогов \n"
          "Р - Работа с каталогом (добавление/удаление книг, просмотр информации о книгах, экспорт каталога) \n"
          "В - Выход из приложения")
    print()
    first_select_action = input("Введите первую букву желаемого действия:     ")
    return first_select_action


# ФУНКЦИИ ВЫВОДА СООБЩЕНИЙ ПРИ СОЗДАНИИ КАТАЛОГА
#___________________________________________________________________________________________________________________
# Вывод сообщения при создании каталога
def message_create_catalog():
    name_catalog = input("Введите название каталога:   ")
    return name_catalog


# Вывод сообщения при уже существующем каталоге либо при успешном создании:
def message_result_create_catalog(value, name_catalog):
    if value == True:
        out_red("Создание нового каталога невозможно! Каталог уже существует!!!")
        print()
    else:
        out_yellow(f"Каталог под названием <<{name_catalog}>> успешно создан!")
        print()


# ФУНКЦИИ ВЫВОДА СООБЩЕНИЙ ПРИ УДАЛЕНИИ КАТАЛОГА
#____________________________________________________________________________________________________________________
# Вывод сообщения при удалении каталога (подтверждение удаления)
def message_confirm_delete_catalog():
    confirm_delete_catalog = input("каталог будет полностью удален, останется лишь статистическая информация.\n"
                                   "Вы точно хотите удалить каталог?? (Да или Нет) :    ")
    return confirm_delete_catalog


# Вывод сообщения результатов удалении каталога
def message_result_delete_catalog(result_delete):
    if result_delete == True:
        out_yellow("Каталог успешно удален!!!")
        print()
    else:
        out_red("Текущий рабочий каталог отсутствует. Нечего удалять")
        print()


# ФУНКЦИИ ВЫВОДА СООБЩЕНИЙ при просмотре истории каталогов
#_____________________________________________________________________________________________________________________
# Вывод сообщения при просмотре истории каталогов
def message_catalogs_history(file):
    file = open(file, "r")
    list = []
    lst_catalog = file.readline()
    list = lst_catalog.split(" ")
    list.pop()
    print(f"За время функционирования программы было создано {len(list)}  каталогов (включая текущий):  ")
    print()
    for i, line in enumerate(list):
        out_yellow(f"{i + 1}. Каталог с именем <<{line}>>")


#_______________________________________________________________________________________________________________________
# Вывод сообщения при работе с каталогом
def msg_select_act_in_catalog():
    print()
    print("Пожалуйста, с помощью ввода начальных букв выберете желаемое действие со списком книг: \n"
          "Д - Добавить книгу в каталог\n"
          "У - Удалить книгу из каталога\n"
          "О - Отобразить все книги каталога \n"
          "П - Поиск книги в каталоге \n"
          "С - Сортировка книг в каталоге \n"
          "Э - Экспорт списка книг из каталога \n"
          "Н - Назад в главное меню")
    print()
    select_act_in_catalog = input("Введите первую букву желаемого действия:     ")
    return select_act_in_catalog


# Вывод сообщения об отсутсвии каталога и предложении использовать тестовый

def msg_offer_create_or_use_test_catalog():
    print()
    out_red("Каталог отсутствует! Необходимо создание нового каталога либо возможно использование тестового\n"
          "Пожалуйста, нажмите: \n"
          "Н - (Назад) для возврата в предыдущее меню и создания каталога\n"
          "Т - использовать тестовый каталог")
    select_user = input("Введите первую букву желаемого действия:     ")
    return select_user

# Вывод сообщения об отсутствии каталогов
def empty_reestr():
    print()
    out_red("Еще ни одного каталога не создавалось. Создайте каталог либо используйте тестовый\n"
          "Н - Назад (к созданию файла) \n"
          "Т - использовать тестовый файл")
    select_user_empty = input("Введите первую букву желаемого действия (Н или Т:     ")
    return  select_user_empty

# Вывод сообщения при добавлении книги
def message_add_book():
    name_book = input("Введите название книги:   ")
    author_book = input("Введите автора книги:   ")
    year_book = input("Введите год издания книги:   ")
    genre_book = input("Введите жанр книги:   ")
    out_yellow("Книга успешно добавлена в каталог!")
    return name_book, author_book, year_book, genre_book


# Вывод сообщения при отображении книг в каталоге
def view_list_books(file):
    catalog = []
    table = []
    file = open(file, "r")
    catalog = file.readlines()
    for i, line in enumerate(catalog, start=1):
        line = line.split(" - ")
        line.insert(0, i)
        table.append(line)
    print_table = tabulate(table, headers=["Номер п/п","Автор","Название","Год издания","Жанр"])
    out_yellow(print_table)
    file.close()


# Вывод сообщения при выборе  книги для удаления
def message_delete_book():
    number_delete_book = int(input(f"Введите порядковый номер книги, которую Вы хотите удалить или 0 для отмены действия:     "))
    return number_delete_book


# Вывод сообщения при выборе поиска книги
def message_search_books():
    search_word = input(f"Введите букву либо часть слова названия книги или ее автора, которую Вы хотите найти:     ")
    return search_word


# Функция вывода списка
def print_list(lst):
    print()
    table = []
    for line in lst:
        line = line.split(" - ")
        table.append(line)
    print_table = tabulate(table, headers=["Автор","Название","Год издания","Жанр"])
    out_yellow(print_table)


def print_list_with_search_word(lst,search_word):
    print("Хотите увидеть искомые слова в выведенных книгах??\n"
          "Д - Да\n"
          "Н - Нет")
    result_select = input("Введите первую букву действия   >>> ")
    if result_select == "Д":
        for line in lst:
            line = line.split(search_word)
            for i in range(len(line)-1):
                print('\033[33m{}\033[0m'.format(line[i]), end="")
                print('\033[31m{}\033[0m'.format(search_word), end="")
            print('\033[33m{}\033[0m'.format(line[-1]), end="")
    return


# Вывод сообщения при выборе сортировки списка книг
def message_sort_books():
    print("По выбранному атрибуту список книг будет отсортирован в порядке возрастания.\n"
          "Перечень атрибутов сортировки:     \n"
          "Н - Название книги\n"
          "А - Автор книги\n"
          "Г - Год издания книги \n"
          "Ж - Жанр книги")
    print()
    sort_atribute = input(f"По выбранному атрибуту список книг будет отсортирован в порядке возрастания.\n"
                          f"Введите первую букву атрибута сортировки списка: ")
    return sort_atribute


# Вывод сообщения при выборе экспорта каталога
def message_result_export_catalog():
    out_yellow("Файл успешно экспортирован в формат CSV!")
    print()

# функции окраски цветом
def out_red(text):
    print("\033[31m {}\033[0m" .format(text))

def out_yellow(text):
    print("\033[33m {}\033[0m" .format(text))