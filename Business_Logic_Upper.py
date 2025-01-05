from Business_Logic_Lower import *





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

    #elif:
    #return
        #action == "Р":
        #action_in_catalog = msg_select_act_in_catalog()
        #while action_in_catalog != "Н":
            #if action_in_catalog == "Д":
            #elif action_in_catalog == "У":
            #elif action_in_catalog == "О":
            #elif action_in_catalog == "П":
            #elif action_in_catalog == "С":
            #elif action_in_catalog == "Э":
    #pass




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