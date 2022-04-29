# Lab Professor: Ms.Laily Ajellu
employee_list = [[1001, "John Alber", "hourly", 8, 0, 0, 22737],
                 [1002, "Sarah Rose", "manager", 12, 0, 0, 22344],
                 [1003, "Alex Folen", "manager", 5, 0, 0, 22957],
                 [1004, "Pola Sahari", "hourly", 17, 0, 0, 22488]]
item_list = [[11526, "Nike Shoes", 120],
             [11849, "Trampoline", 180],
             [11966, "Mercury Bicycle", 150],
             [11334, "Necklace Set", 80]]
hline_a = " —————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————"
hline_b = " ———————————————————————————————————————————————————————"


def menu():
    menu_layout = """
    —————————————————————————————
    |                           |
    | 1 - Create Employee       |
    |                           |
    | 2 - Create Item           |
    |                           |
    | 3 - Make Purchase         |
    |                           |
    | 4 - All Employee Summary  |
    |                           |
    | 5 - Exit                  |
    |                           |
    —————————————————————————————
                                      """
    print(menu_layout)

    menu_choice = input("Select from the menu: ")
    return menu_choice


def get_user_info():
    new_emp = "yes"
    while new_emp == "yes":

        test_employee_id = False
        while not test_employee_id:
            employee_id = input("Enter Employee ID: ")
            test_employee_id = validate_new_employee(employee_id, "Employee ID", 0)
        employee_id = int(employee_id)

        employee_name = ""
        while employee_name == "":
            employee_name = input("Enter Employee Name: ")
            if employee_name == "":
                print("The \'Employee Name\' cannot be empty.")

        employee_type = input("Enter Employee Type: ").lower()
        while employee_type not in ['manager', 'hourly']:
            print("Invalid input.")
            employee_type = input("Enter 'Manager' or 'Hourly' as Employee Type: ").lower()

        test_years_worked = False
        while not test_years_worked:
            years_worked = input("Enter Years Worked: ")
            test_years_worked = validate_new_employee(years_worked, "Years Worked", 3)
        years_worked = int(years_worked)

        test_employee_discount_number = False
        while not test_employee_discount_number:
            employee_discount_number = input("Enter Employee Discount Number: ")
            test_employee_discount_number = validate_new_employee(employee_discount_number, "Employee Discount Number",
                                                                  6)
        employee_discount_number = int(employee_discount_number)

        employee = [employee_id, employee_name, employee_type, years_worked, 0, 0, employee_discount_number]
        employee_list.append(employee)
        # print(employee_list)
        new_emp = input("Would you like to add another employee? (YES or NO): ").lower()
        while new_emp not in ["yes", "no"]:
            print("Invalid input.")
            new_emp = input("Would you like to add another employee? (YES or NO): ").lower()
    return_menu()


def validate_new_employee(val, msg, pos):
    if val == "":
        print("The \'" + msg + "\' cannot have empty value.")
        return False
    if not val.isnumeric():
        print("The \'" + msg + "\' must be number.")
        return False
    if pos == 0 or pos == 6:
        val_num = int(val)
        for emp in employee_list:
            if val_num == emp[pos]:
                print("The \'" + msg + "\' must be unique.")
                return False
    return True


def get_item_info():
    new_item = "yes"
    while new_item == "yes":

        test_item_number = False
        while not test_item_number:
            item_number = input("Enter Item Number: ")
            test_item_number = validate_new_item(item_number, "Item Number", 0)
        item_number = int(item_number)

        item_name = ""
        while item_name == "":
            item_name = input("Enter Item Name: ")
            if item_name == "":
                print("The \'Item Name\' cannot be empty.")

        test_item_cost = False
        while not test_item_cost:
            item_cost = input("Enter Item Cost: ")
            test_item_cost = validate_new_item(item_cost, "Item Cost", 2)
        item_cost = float(item_cost)

        item = [item_number, item_name, item_cost]
        item_list.append(item)
        new_item = input("Would you like to add another item? (YES or NO): ").lower()
        while new_item not in ["yes", "no"]:
            print("Invalid input.")
            new_item = input("Would you like to add another item? (YES or NO): ").lower()
    return_menu()


def validate_new_item(val, msg, pos):
    if val == "":
        print("The \'" + msg + "\' cannot have empty value.")
        return False

    if pos == 0:
        if not val.isnumeric():
            print("The \'" + msg + "\' must be number.")
            return False
        val_num = int(val)
        for item in item_list:
            if val_num == item[pos]:
                print("The \'" + msg + "\' must be unique.")
                return False
    if pos == 2:
        try:
            val_float = float(val)
        except:
            print("The \'" + msg + "\' must be number.")
            return False

    return True


def item_summary():
    print()
    print(hline_b)
    print("|    Item Number    |    Item Name     |   Item Cost    |")
    print(hline_b)
    for itm in item_list:
        print("|", str(itm[0]).center(17), "|", str(itm[1]).center(16), "|", ("$" + str(format(itm[2], ".2f"))).center(14), "|")
        print(hline_b)
    print()
    new_purchase = "yes"
    while new_purchase == "yes":
        employee_purchase()
        new_purchase = input("Would you like to make another purchase? (YES or NO): ").lower()
        while new_purchase not in ["yes", "no"]:
            print("Invalid input.")
            new_purchase = input("Would you like to make another purchase? (YES or NO): ").lower()
    display_employees()


def employee_purchase():
    valid_EDN = False
    while not valid_EDN:
        purchase_discount_number = input("Enter Employee Discount Number: ")
        x = 0
        for emp in employee_list:
            if str(emp[6]) == purchase_discount_number:
                valid_EDN = True
                break
            x = x + 1
        if not valid_EDN:
            print("This \'Employee Discount Number\' does not exist.")

    valid_IN = False
    while not valid_IN:
        purchase_item_number = input("Enter Item Number for Purchase: ")
        y = 0
        for itm in item_list:
            if str(itm[0]) == purchase_item_number:
                valid_IN = True
                break
            y = y + 1
        if not valid_IN:
            print("This \'Item Number\' does not exist.")

    confirm = input("Do you confirm the purchase of item " + item_list[y][1] + " for employee " + employee_list[x][
        1] + "? (YES or NO): ").lower()
    while confirm not in ["yes", "no"]:
        print("Invalid input.")
        confirm = input("Do you confirm the purchase of item " + item_list[y][1] + " for employee " + employee_list[x][
            1] + "? (YES or NO): ").lower()
    if confirm == "yes":
        discount_percent = 2 * employee_list[x][3]
        if discount_percent > 10:
            discount_percent = 10
        if employee_list[x][2] == "manager":
            discount_percent = discount_percent + 10
        else:
            discount_percent = discount_percent + 2
        discount = item_list[y][2] * discount_percent / 100
        total_discount = discount + employee_list[x][5]
        if total_discount >= 200:
            discount = discount - (total_discount - 200)
        print("Discount percent: ", discount_percent, "%")
        print("Discount amount: $", round(discount, 2))
        print("Purchase amount: $", round(item_list[y][2] - discount, 2))
        total_purchase = item_list[y][2] - discount + employee_list[x][4]
        total_discount = discount + employee_list[x][5]
        employee_list[x][4] = round(total_purchase, 2)
        employee_list[x][5] = round(total_discount, 2)


def display_employees():
    print()
    print(hline_a)
    print(
        "| Employee ID | Employee Name | Employee Type | Years Worked | Total Purchased | Total Discount | Employee Discount Number |")
    print(hline_a)
    for emp in employee_list:
        print("|", str(emp[0]).center(11), "|", emp[1].center(13), "|", emp[2].center(13), "|", str(emp[3]).center(12),
              "|", ("$ " + str(emp[4])).center(15), "|", ("$ " + str(emp[5])).center(14), "|", str(emp[6]).center(24),
              "|")
        print(hline_a)
    print()
    return_menu()


def return_menu():
    print()
    choice = input("Would you like to return to the menu? (YES or NO): ").lower()
    while choice not in ["yes", "no"]:
        print("Invalid input.")
        choice = input("Would you like to return to the menu? (YES or NO): ").lower()
    if choice == "no":
        exit()
