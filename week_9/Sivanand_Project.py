import db_base as db

class Employee:
    def __init__(self,name,department,role):
        self.name=name
        self.department=department
        self.role=role

class HourlyEmployee(Employee):# Inherits from Employee class
    def __init__(self,name,department,hourly_salary,num_hours,role="HourlyEmployee"):
        Employee.__init__(self,name,department,role)
        self.hourly_salary=hourly_salary
        self.num_hours=num_hours

    def info(self):# Specific to HourlyEmployee class
        return self.name,self.department,self.role,self.hourly_salary*self.num_hours

class SalariedEmployee(Employee):# Inherits from Employee class
    def __init__(self,name,department,base_monthly_salary):
        Employee.__init__(self,name,department,"SalariedEmployee")
        self.base_monthly_salary=base_monthly_salary

    def info(self):# Specific to SalariedEmployee class
        return self.name,self.department,self.role,self.base_monthly_salary


class Manager(Employee):# Inherits from Employee class
    def __init__(self, name,department, base_monthly_salary,role="Manager"):
        Employee.__init__(self, name, department,role )
        self.base_monthly_salary = base_monthly_salary

    def info(self):# Specific to Manager class
        return self.name, self.department, self.role, self.base_monthly_salary*1.5

class Executive(Employee):# Inherits from Employee class
    def __init__(self, name, department, base_monthly_salary,role="Executive"):
        Employee.__init__(self, name,department, role)
        self.base_monthly_salary = base_monthly_salary

    def info(self):#Specific to Executive class
        return self.name, self.department, self.role, self.base_monthly_salary*1.75




class Company(db.DBbase):
    def __init__(self):
        super().__init__("Company.sqlite")
        self.connect()

    def hire(self,name,department,role):
        if role.lower()=="HourlyEmployee".lower():
            self.hourly_salary=int(input("Enter Hourly salary of "+name+": "))
            self.num_hours=int(input("Enter number of hours working per month: "))
            name,department,role,salary=HourlyEmployee(name, department, self.hourly_salary, self.num_hours).info()
            self.__add_employee(name,department,role,salary)
        elif role.lower()=="SalariedEmployee".lower():
            self.base_monthly_salary=int(input("Enter department base monthly salary of "+name+": "))
            name, department, role, salary =SalariedEmployee(name, department, self.base_monthly_salary).info()
            self.__add_employee(name, department, role, salary)
        elif role.lower()=="Manager".lower():
            self.base_monthly_salary=int(input("Enter department base monthly salary of "+name+": "))
            name, department, role, salary = Manager(name, department, self.base_monthly_salary).info()
            self.__add_employee(name, department, role, salary)
        elif role.lower()=="Executive".lower():
            self.base_monthly_salary=int(input("Enter department base monthly salary of "+name+": "))
            name, department, role, salary = Executive(name, department,self.base_monthly_salary).info()
            self.__add_employee(name, department, role, salary )

    def fire(self, name, department,role="Employee"):
        try:
            self.__delete_employee(name, department)
        except Exception as e:
            print("An error occurred.", e)

    def raise_emp(self, name, department, type="salary"):
        if type.lower()=="role":
            self.role=input("Enter the new role\n\rtype one of HourlyEmployee/Executive/SalariedEmployee/Manager: ")
            self.__update_employee_role_salary(name,department,self.role)
        elif type.lower()=="salary":
            self.role=self.fetch_role(name,department) # fetching current role
            self.__update_employee_role_salary(name, department, self.role)

    def __add_employee(self,name,department,role,salary): #Private method
        try:
            super().connect()
            super().get_cursor.execute("""insert or ignore into Employee (name,department,role,salary) values(?,?,?,?);""", (name,department,role,salary,))
            super().get_connection.commit()
            super().close_db()
            print("Hired {0} for {1} department successfully".format(name,department))
        except Exception as e:
            print("An error occurred.", e)


    def __delete_employee(self, name,department): #Private method
        try:
            super().connect()
            super().get_cursor.execute("""delete from Employee where name=? and department=?;""",(name,department,))
            super().get_connection.commit()
            super().close_db()
            print("deleted employee",name,"successfully")
        except Exception as e:
            print("An error occurred.", e)

    def __update_employee_role_salary(self,name,department,role): #Private method
        if role.lower() == "HourlyEmployee".lower():
            self.hourly_salary = int(input("Enter Hourly salary of " + name + ": "))
            self.num_hours = int(input("Enter number of hours working per month: "))
            name, department, role, salary = HourlyEmployee(name, department, self.hourly_salary, self.num_hours).info()
            self.__update_employee(name, department, role, salary)
        elif role.lower() == "SalariedEmployee".lower():
            self.base_monthly_salary = int(input("Enter department base monthly salary of " + name + ": "))
            name, department, role, salary = SalariedEmployee(name, department, self.base_monthly_salary).info()
            self.__update_employee(name, department, role, salary)
        elif role.lower() == "Manager".lower():
            self.base_monthly_salary = int(input("Enter department base monthly salary of " + name + ": "))
            name, department, role, salary = Manager(name, department, self.base_monthly_salary).info()
            self.__update_employee(name, department, role, salary)
        elif role.lower() == "Executive".lower():
            self.base_monthly_salary = int(input("Enter department base monthly salary of " + name + ": "))
            name, department, role, salary = Executive(name, department, self.base_monthly_salary).info()
            self.__update_employee(name, department, role, salary)

    def __update_employee(self,name,department,current_role,new_base_salary): #Private method
        try:
            super().connect()
            super().get_cursor.execute("""update Employee set role=?,salary=? where name=? and department=?;""", (current_role,new_base_salary,name,department,))
            super().get_connection.commit()
            super().close_db()
            print("Updated salary of {} successfully".format(name))
        except Exception as e:
            print("An error occurred.", e)



    def fetch(self, id=None):
        try:
            super().connect()
            if id is not None:
                return super().get_cursor.execute("""SELECT * FROM Employee WHERE id=?; """, (id,)).fetchall()
            else:
                return super().get_cursor.execute("""SELECT * FROM Employee ;""").fetchall()
            # if Id is null (or None), then get everything, else get by id
        except Exception as e:
            print("An error occurred.", e)
        finally:
            super().close_db()

    def fetch_role(self,name,department):
        try:
            super().connect()
            self.current_role=super().get_cursor.execute("""SELECT role FROM Employee WHERE name=? and department=?; """, (name,department,)).fetchall()
            return self.current_role[0][0]
        except Exception as e:
            print("An error occurred.", e)
        finally:
            super().close_db()



    def reset_company(self):
       sql= """DROP TABLE IF EXISTS Employee;
               CREATE TABLE Employee(
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
               name TEXT UNIQUE,
               department TEXT,
               role TEXT,
               salary DECIMAL(10,5));"""
       super().execute_script(sql)

def program_start():
    option=input("""Welcome to XXX Company!
Select from the following actions
1.Hire
2.Fire
3.Raise
4.Search\n\rEnter your option: """)
    company=Company()
    if option=="1" or option.lower()=="hire":
        num_employees=int(input("How many employees you want to hire? "))
        for i in range(num_employees):
            name=input("Enter name of the employee: ")
            department=input("In which department you want to hire him in? ")
            role=input("What will be the role of employee?\n\rtype one of HourlyEmployee/Executive/SalariedEmployee/Manager: ")
            company.hire(name,department,role)
            print("")
    if option=="2" or option.lower()=="fire":
        display(company.fetch())
        name = input("Enter name of the employee from the above list: ")
        department = input("Enter the department above employee works in? ")
        role=input("Enter the role of employee?\n\rtype one of HourlyEmployee/Executive/SalariedEmployee/Manager: ) ")
        company.fire(name,department)
    if option=="3" or option.lower()=="raise":
        display(company.fetch())
        name = input("Enter name of the employee from above list: ")
        department = input("Enter the department above employee works in? ")
        type=input(" Are you raising the employee by role or by just salary?, type role or salary : ")
        company.raise_emp(name,department,type)
    if option=="4" or option.lower()=="search":
        id=input("Enter the id of the employee or type None to fecth all employees information? ")
        if id.lower()=="none":
            display(company.fetch())
        elif id.isnumeric():
            display(company.fetch(int(id)))
        else:
            print("Not a valid Id, Try again.")

def display(x):
    print("Current employees list")
    for a, b, c, d, e in x:
        print("Id:", a, ",Employee:", b, ",Department:", c, ",role:", d, ",salary:", e)

program_start()






