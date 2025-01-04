
import GraficUserInterface
from Bussiness_Logic_Lower import *


# функция создания каталога и присвоения ему имени
def create_catalog():
    if exist_catalog() == True:
        return False
    catalog = open(message_create_catalog(), "w")
    return True

