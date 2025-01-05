from Business_Logic_Lower import *



def work_with_catalog(file):
        from GraficUserInterface import msg_select_act_in_catalog, message_add_book
        action_in_catalog = msg_select_act_in_catalog()
        while action_in_catalog != "Н":
            if action_in_catalog == "Д":
                name_book, author_book, year_book, genre_book = message_add_book()
                add_book(file, name_book, author_book, year_book, genre_book)
pass
            #elif action_in_catalog == "У":
            #elif action_in_catalog == "О":
            #elif action_in_catalog == "П":
            #elif action_in_catalog == "С":
            #elif action_in_catalog == "Э":


# ФУНКЦИЯ НЕПОСРЕДСТВЕННОГО ФУНКЦИОНИРОВАНИЯ ПРОГРАММЫ ПРИ ВЫБОРЕ ПОЛЬЗОВАТЕЛЯ

def global_function(action):
    from GraficUserInterface import message_first_select
    if action == "С":
        from GraficUserInterface import message_create_catalog, message_result_create_catalog
        result_exist = exist_catalog()
        name_catalog = None
        if result_exist == False:
            name_catalog = message_create_catalog()
            create_catalog(name_catalog)
            reestr_catalog(name_catalog)
        return message_result_create_catalog(result_exist, name_catalog)

    elif action == "У":
        from GraficUserInterface import message_confirm_delete_catalog, message_result_delete_catalog, message_first_select, message_create_catalog
        if message_confirm_delete_catalog() == "Да":
            result_exist = exist_catalog()
            if result_exist == True:
                delete_catalog()
            return message_result_delete_catalog(result_exist)

        elif message_confirm_delete_catalog() == "Нет":
            message_first_select()

    elif action == "П":
        from GraficUserInterface import message_catalogs_history
        message_catalogs_history(list_catalog)

    elif action == "Р":
        result_exist = exist_catalog()
        if result_exist == True:
            path = os.getcwd()
            work_file = None
            for work_file in os.listdir(path):
                if work_file.endswith(".txt"):
                    return work_file
            work_with_catalog(work_file)
        else:
            print("КАталог книг отсутствует. Для начала создайте каталог!")





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
    file.write(name_book + author_book + year_book + genre_book)
    file.close()

# функция удаления книги из каталога


# функция для отображения списка книг (каталога)
def view_catalog(file):
    catalog = []
    file = open(file, "r")
    catalog = file.readlines()
    for line in catalog:
        print(line)
        print()

# функция поиска книги в каталоге

# функция сортировки книги в каталоге

# функция экспорта каталога