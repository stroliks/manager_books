import os
from Business_Logic_Upper import *


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
