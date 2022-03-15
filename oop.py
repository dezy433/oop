


class Employee:
    def __init__(self, name, l_name, position, year, month, birth_day, graduate, ids):
        self.first_name = name
        self.last_name = l_name
        self.position = position
        self.year = year
        self.month = month
        self.birth_day = birth_day
        self.graduate = graduate
        self.id = ids

    def self_first_name(self, name):
        self.first_name = name

    def self_last_name(self, last_name):
        self.last_name = last_name

    def self_birth_year(self, birth_year):
        self.birth_year = birth_year

    def self_birth_month(self, birth_month):
        self.birth_month = birth_month

    def self_birth_day(self, day):
        self.day = day

    def self_position(self, position):
        self.position = position

    def self_graduated(self, new_graduate):
        self.graduate = new_graduate

    def set_ids(self, ids):
        self.id = ids

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_birth_year(self):
        return self.birth_year

    def get_birth_month(self):
        return self.birth_month

    def get_birth_day(self):
        return self.day

    def get_position(self):
        return self.position

    def get_graduate(self):
        return self.graduate

    def get_id(self):
        return self.id

    def __str__(self):
        return f"'first_name': '{self.first_name}', 'last_name': '{self.last_name}', 'birth_year':'{self.birth_year}', 'birth_month':'{self.birth_month}', 'birth_day': '{self.birth_day}', 'emp_position':'{self.position}', 'is_graduated': '{self.graduate}', 'id': '{self.id}'"


def select_option():
    while True:
        user_option = input(
            "This is a list of your options: 1: Add an Employee, 2: Remove an Employee, 3: List the Employees ,4: Update Employee Data, 5: Exit the app")
        user_option = user_option.strip()
        if user_option in ["1", "2", "3", "4", "5","6"]:
            return user_option
        else:
            print("Error, You should select one of the options in the list")


def id_func():
    while True:
        id_str = input("Insert ID")
        if id_str.isdigit():
            id_int = int(id_str)
            # self.ids = id_int
            return id_int
        else:
            print("Add numbers")


def first_name_func():
    while True:
        name = str(input("name"))
        if len(name.strip()) > 2:
            return name


def last_name_func():
    while True:
        l_name = str(input("Last name"))
        if len(l_name.strip()) > 2:
            return l_name


def birth_year_func():
    while True:
        birth_year_str = input("Birth Year")
        if birth_year_str.isdigit():
            birth_year = int(birth_year_str)
        if (birth_year >= 1900) and (birth_year <= 2004):
            # self.birth_year= birth_year
            return birth_year
        else:
            print("Years ranging from 1990-2004")


def birth_month_func():
    while True:
        birth_month_str = input("Birth month")
        if birth_month_str.isdigit():
            birth_month = int(birth_month_str)
        if (birth_month >= 1) and (birth_month <= 12):

            return birth_month
        else:
            print("Please enter as a number between 1 and 12")


def bday_func():
    while True:
        bday_str = input("Birth Day ")
        if bday_str.isdigit():
            bday = int(bday_str)
        if (bday >= 1) and (bday <= 31):

            return bday
        else:
            print("Please enter as a number between 1 and 31")


def position_func():
    while True:
        position_str = input("Position")
        if len(position_str.strip()) > 2:
            position = str(position_str)
            # self.position = position_str
            return position
        else:
            print("Please enter your position")


def graduate_func():
    answers = ["yes", "no", "Yes", "No"]
    while True:
        graduate_str = input("Have you graduatd?")
        if graduate_str in answers:

            return graduate_str
        else:
            print("Please answer 'Yes' or 'No'")


def create_employee():
    employee_first_name = first_name_func()
    employee_last_name = last_name_func()
    employee_position = position_func()
    employee_birth_year = birth_year_func()
    employee_birth_month = birth_month_func()
    employee_birth_day = bday_func()
    employee_is_graduated = graduate_func()
    employee_id = id_func()

    employee = Employee(employee_first_name, employee_last_name, employee_birth_year, employee_birth_month,
                        employee_birth_day, employee_position, employee_is_graduated, employee_id)

    return employee


def add_employee():
    employee = create_employee()
    employee_db[employee.get_id()] = employee
    print("added")

def employee_db():
    global employee_db
    for entry in employee_db:
        print(employee_db[entry])
        employee = create_employee()
        employee_db[employee.get_id()] = employee


def del_employee():
    del_employee_id = (input("Enter Employee ID: "))
    if del_employee_id.isdigit():
        for ids in range(len(employee_db)):
            if employee_db[ids]['Employee ID'] == del_employee_id:
                del employee_db[ids]
                return employee_db
            else:
                print("Employee ID doesnt exist")


def print_all_employee():
    for employee_id_key in employee_dict:
        print(f"The data of the employee with Employee_ID = {employee_id_key}")
        print(employee_dict[employee_id_key])


def read_field_option():
    while True:
        field_option = input(
            "Please Enter the field you want to update: first_name, last_name, position, birth_year, birth_month, birth_day, is_graduated:")
        field_option = field_option.strip()
        if field_option in ["first_name", "last_name", "position", "birth_year", "birth_month", "birth_day",
                            "is_graduated"]:
            return field_option
        else:
            print("Please enter one of the mentioned fields")


def list_employees_data():
    for employee_id_key in employee_dict:
        print(f"The data of the employee with Employee_ID = {employee_id_key}")
        print(employee_dict[employee_id_key])


def update(employee_id):
    field_option = select_option()
    if field_option == "first_name":
        new_first_name = first_name_func()
        employee_dict[employee_id]["first_name"] = new_first_name
    elif field_option == "last_name":
        new_last_name = last_name_func()
        employee_dict[employee_id]["last_name"] = new_last_name
    elif field_option == "position":
        new_position = position_func()
        employee_dict[employee_id]["employee_position"] = new_position
    elif field_option == "birth_year":
        new_birth_year = birth_year_func()
        employee_dict[employee_id]["birth_year"] = new_birth_year
    elif field_option == "birth_month":
        new_birth_month = birth_month_func()
        employee_dict[employee_id]["birth_month"] = new_birth_month
    elif field_option == "birth_day":
        new_birth_day = bday_func()
        employee_dict[employee_id]["birth_day"] = new_birth_day
    elif field_option == "graduate":
        new_graduate = graduate_func()
        employee_dict[employee_id]["is_graduated"] = new_graduate
    else:
        print("Update sucessfull")


if __name__ == '__main__':
    print("Select operation.")
    print("1.Add an Employee")
    print("2.Remove employee")
    print("3.Get a list of employees")
    print("4.Retreive employee (By ID)")
    print("5.Update employee data")
    print("6.Quit")



    employees_list = []

    employee_dict = {}
    options = select_option()
    while True:
        if options == "1":
            print("The user wants to add an Employee")
            employee_object = create_employee()
        print(employee_dict.get(employee_db))

        elif options == "2":
        print("Do you want to delete a user")
        employee_id = id_func()
        del employee_dict[employee_id]

        elif options == "3":
        list_employees_data()

        elif options == "4":
        print("Update the employee")
        employee_id = id_func()
        update(employee_id)
        elif options == "5":
            print("Get empoyee by ID")
        elif options == 6:
            break
        else:
            print("choose from 1,2,3,4,5,6")

