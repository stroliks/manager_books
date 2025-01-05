import os
from Business_Logic_Upper import *


# функция проверки существования каталога перед созданием каталога
def exist_catalog():
    path = os.getcwd()
    for file in os.listdir(path):
        if file.endswith(".txt"):
            return True
    return False

# функция ведения реестра созданных каталогов
list_catalog = []
def reestr_catalog(name_catalog):
    list_catalog.append(name_catalog)
