
import GraficUserInterface
from Bussiness_Logic_Lower import *



# ФУНКЦИИ ПРИ СОЗДАНИИ КАТАЛОГА
#___________________________________________________________________________________________________________________
# функция создания каталога и присвоения ему имени
def create_catalog():
    if exist_catalog() == True:
        return False
    list_catalog = []
    name_catalog = message_create_catalog()
    catalog = open(name_catalog, "w")
    list_catalog.append(name_catalog)
    return True

# ФУНКЦИИ ПРИ УДАЛЕНИИ КАТАЛОГА
#____________________________________________________________________________________________________________________