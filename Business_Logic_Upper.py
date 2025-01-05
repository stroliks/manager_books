
import GraficUserInterface
from Bussiness_Logic_Lower import *

###name_catalog = message_create_catalog()

# ФУНКЦИИ ПРИ СОЗДАНИИ КАТАЛОГА
#___________________________________________________________________________________________________________________
# функция создания каталога и присвоения ему имени
def create_catalog(name_catalog):
    catalog = open(name_catalog, "w")
    return True

# функция учета созданных каталогов
def list_catalog(name_catalog):
    list_catalog.append(name_catalog)
    return list_catalog



# ФУНКЦИИ ПРИ УДАЛЕНИИ КАТАЛОГА
#____________________________________________________________________________________________________________________
# функция удаления каталога
def delete_catalog(name_catalog):
    os.remove(name_catalog)