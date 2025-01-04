import os


# функция проверки существования каталога перед созданием каталога
def exist_catalog():
    return os.path.isfile(".txt")
