# Lab Professor: Ms.Laily Ajellu
from function import *

while True:
    menu_choice = menu()
    if menu_choice == "1":
        print()
        print("------------------------Create Employee------------------------")
        get_user_info()
    if menu_choice == "2":
        print()
        print("--------------------------Create Item-------------------------")
        get_item_info()
    if menu_choice == "3":
        print()
        print("-------------------------Make Purchase-------------------------")
        item_summary()
    if menu_choice == "4":
        print()
        print("----------------------All Employee Summary----------------------")
        display_employees()
    if menu_choice == "5":
        exit()
