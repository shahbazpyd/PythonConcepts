# class Employee:
    
#     def __init__(self, emp_id, name, salary):
#         self.emp_id = emp_id
#         self.name = name
#         self.salary = salary

#     def display_details(self):
#         print("Employee ID:", self.emp_id)
#         print("Name: ", self.name)
#         print("Salary: ", self.salary)

#     def increase_salary(self, amount):
#         self.salary += amount

# emp1 = Employee(101, "Shahbaz", 30000)
# emp1.display_details()

# emp1.increase_salary(5000)

# emp1.display_details()




# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name: ",self.name )
#         print("Name: ", self.age)

# student1 = Student("Shahbaz", 22)
# student1.display()



# class Employee:
#     def role(self):
#         print("I am an Employee")

# class Manager(Employee):
#     def role(self):
#         print("I am an Manager")
#         super().role()

# obj = Manager()
# obj.role()



# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def display_employee(self):
#         print("Name: ", self.name)
#         print("Salary: ", self.salary)

# class Developer(Employee):
#     def __init__(self, name, salary, language):
#         super().__init__(name, salary)
#         self. language = language

#     def display_developer(self):
#         print("Programming Language: ", self.language)

# dev = Developer("Shahbaz", 50000, "Python")
# dev.display_employee()
# dev.display_developer()

    


# Start

# Create a class
class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self._balance = balance   # private variable (by convention)

    # Method to read private data
    def get_balance(self):
        return self._balance

    # Method to modify private data
    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient balance")

# Create object of the class
account = BankAccount("Shahbaz", 10000)

# Access data only through methods
print("Initial Balance:", account.get_balance())

account.deposit(2000)
print("After Deposit:", account.get_balance())

account.withdraw(3000)
print("After Withdrawal:", account.get_balance())

# Stop
