import os
from Business_Logic_Upper import *

# функция определения имени последнего каталога
def name_catalog():
    file = open("Реестр каталогов.txt", "r")
    lst_catalog = file.readlines()
    lengt_catalog = len(lst_catalog)
    if lengt_catalog == 0:
        return None
    name_catalog = lst_catalog[lengt_catalog - 1]
    file.close()
    return name_catalog

# функция проверки существования реестра каталогов
def exist_reestr():
    path = os.getcwd()
    if "Реестр каталогов.txt" in os.listdir(path):
        return True
    return False


# функция проверки существования каталога перед созданием каталога
def exist_catalog():
    filename = name_catalog()
    path = os.getcwd()
    if filename in os.listdir(path):
        return True
    return False


# функция ведения реестра созданных каталогов

def reestr_catalog(name_catalog):
    list_catalog = open(f"Реестр каталогов.txt", "a")
    list_catalog.write(name_catalog)
    list_catalog.close()
    return list_catalog
