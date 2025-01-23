# """
# Polymorphism:  'Many-forms'

# it is a ability of a python object to behave differently in different
# situations.
# Ex: A function behaving differently to different type of arguments
# Overloading: The method name is the same, but the method signature (parameters) is different.
# Overriding: A subclass provides its own implementation for a method inherited from the superclass, typically with the same signature.

# """

# + is python objects

# with ints
# 1
print(1 + 2)

print("a" + "b")
"""
Here the + opertaor is behaving differently to diffrent type of inputs .
for  2 int objects it will add  and for 2 str objects it will concatinate
"""
# 2
print(len("sachin"))  # for string inputs  t will return number of chrs present

print(len(["23", "3", "231"]))  # for lists it will returns number of items

dict_1 = {"sachin": "km", "guru": "yadki", "veeru": "AM"}

print(len(dict_1))  # here also it will count the number of items

# 3
str_re = reversed("sachin")
print(str_re)

for s in str_re:
    print(s)

dict_re = reversed(dict_1)
print(dict_re.__next__())

for value in dict_re.__iter__():
    print(value)

#######################################################
# 4


def add(x, y, z=0):
    return x + y + z


# Driver code
print(add(2, 3))
# print(add(2, 3, 4))


class Calculator:
    def add(self, *args):  # Accepts a variable number of arguments
        return sum(args)


# Creating an instance of Calculator
calc = Calculator()

# Calling the method with different numbers of arguments
print(calc.add(1))  # 1
print(calc.add(1, 2))  # 3
print(calc.add(1, 2, 3, 4))  # 10


# ###################################################
# # Example : Payment System


# Method Overirding
class PaymentMethod:
    def process_payment(self, amount):
        raise NotImplementedError("Subclasses should implement this method")


class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"processing credit card payment of ${amount}")


class PaypalPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"process Paypal Payment of ${amount}")


class BankTransferPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"process Bank Transfer Payment of ${amount}")


def make_payment(payment_method, amount):
    payment_method.process_payment(amount)  # classname.methodname()


payment_methods = [CreditCardPayment(), PaypalPayment(), BankTransferPayment()]

for payment_method in payment_methods:
    make_payment(payment_method, 100)

#     #######################################
"""
Method Overriding: 
    In Python, Polymorphism lets us define methods in the child class that have the same name 
    as the methods in the parent class. In inheritance, the child class inherits the methods 
    from the parent class. However,it is possible to modify a method in a child class that it 
    has inherited from the parent class. 
    This is particularly useful in cases where the method inherited from the parent class 
    doesn’t quite fit the child class.
    In such cases, we re-implement the method in the child class. 
    This process of re-implementing a method in the child class is known as Method Overriding.  
"""


class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")


class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")


class ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")


obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()

# #######################################
