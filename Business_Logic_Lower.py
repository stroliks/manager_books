import os
from Business_Logic_Upper import *

# функция определение имени последнего каталога
def name_catalog():
    file = open(f"Реестр каталогов.txt", "r")
    lst_catalog = file.readlines()
    lengt_ctalog = len(lst_catalog)
    name_catalog = lst_catalog[lengt_ctalog - 1]
    return name_catalog


# функция проверки существования каталога перед созданием каталога
def exist_catalog():
    path = os.getcwd()
    for file in os.listdir(path):
        if file.endswith(".txt") and file:
            return True
    return False


# функция ведения реестра созданных каталогов

def reestr_catalog(name_catalog):
    list_catalog = open(f"Реестр каталогов.txt", "a")
    list_catalog.write(name_catalog)
    list_catalog.close()
    return True
