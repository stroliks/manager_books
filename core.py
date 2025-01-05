import GraficUserInterface
import Bussiness_Logic_Upper

greeting()
first_select_action = message_first_select()
while first_select_action != "В":
    global_function(first_select_action)