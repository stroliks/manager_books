from GraficUserInterface import *
from Business_Logic_Upper import *


def start_programm():
    greeting()
    first_select_action = message_first_select()
    while first_select_action != "В":
        global_function(first_select_action)
        first_select_action = message_first_select()
    goodbye()
