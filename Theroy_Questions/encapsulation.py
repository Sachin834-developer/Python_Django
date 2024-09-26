"""
Encapsulation: Encapsulation is a mechanism of wrapping the data (variables) and code acting on 
the data (methods) together as a single unit. In encapsulation, the variables of a class will
be hidden from other classes,and can be accessed only through the methods of their current class.

To avoid accidental modification of the data by make use of access modifiers.
restricting the access to class properties and methods is called encapsulation.

Access Modifiers :Access specifiers in Python have an important role to play in securing data
from unauthorized access and in preventing it from being exploited.
using these we restrict the data access outside of the class in encapsulation.

Public: can access outside or inside of the class using object reference.

Private: can only access these variables inside the class  __privatevariable (2 underscores) .
            we can access these with the use of methods in the class.

Protected: accessable within the classes and its subclasses  _protected

When we use __privatevar in a class , after the intialisation python creates that variable with '_classname__variablename'
ex : _Company__revenue 
 to acess this outside of the class objectname._ClassName__VariableName    Ex: company_1._Company__revenue


"""


class Company:

    def __init__(self, name, revenue, location):
        self.name = name
        self.__revenue = revenue  # private var
        self._location = location  # protected var

    def display(self):
        print(
            f"{self.name} has overall revenue of {self.revenue} at {self.location} location"
        )

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Company({self.name},{self.revenue},{self.location})"

    # @property
    def __display_revenue(
        self,
    ):  # now its a private method  , same logic as private variable
        return self.__revenue


company_1 = Company("tcs", 300000, "Bangalore")
print(company_1._Company__revenue)  # accessing the private variable
print(company_1.__dir__())
# print(company_1.__display_revenue())  # accessing the private method
print(company_1._location)


class Manager(Company):
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary
        # company_1.revenue=200000
        print(
            self.name
        )  # check this unable to access the protected var here inside child class
        super().__init__(name, salary, "bangalore")

    def display_location(self):
        print(self._location)


mgr_1 = Manager("sachin", "30000")
print(dir(Manager))
print(mgr_1.display_location())


# EXAMPLE 2

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public attribute
        self.__balance = balance  # Private attribute
    
    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")
    
    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")
    
    # Public method to check balance (encapsulated through a method)
    def get_balance(self):
        return self.__balance

# Creating an instance of BankAccount
account = BankAccount("Alice", 1000)

# Accessing public methods
account.deposit(500)
account.withdraw(200)
print("Balance:", account.get_balance())

# Trying to access private attribute directly (will raise an error)
# print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'

# Accessing private attribute (not recommended, for demonstration)
print("Balance accessed using name mangling:", account._BankAccount__balance)
