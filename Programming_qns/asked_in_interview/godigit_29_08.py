"""
29/08/2024  --1st Round
COMPANY: DIGIT INSURANCE

ROLE: PYTHON DEVELOPER

NEED for Company : Python dev to write automation scripts and to develope API's using  python ,
 Django, Fastapi

Python QNs:

    Explain with code examples all OOPS Concepts , real world usecases
    Decorator with example , usecases
    Access Modifiers
    Python Datatypes 
    Asyncio module

Django:
     ORM
     Model relationships

"""
#coding qns 
# Add Quntities of products if name of product is same , and ouput in the same format
"""
OUTPUT

[
    {'name': 'product1', 'desc': 'random desc', 'quantity': 30},
    {'name': 'product2', 'desc': 'random desc', 'quantity': 20},
    {'name': 'product4', 'desc': 'random desc', 'quantity': 50},
    {'name': 'product5', 'desc': 'random desc', 'quantity': 50}
]

"""

product_list = [
    {
        'name':'product1',
        'desc': 'random desc',
        'quantity' : 10
                },
                {
        'name':'product2',
        'desc': 'random desc',
        'quantity' : 20
                },
                {
        'name':'product1',
        'desc': 'random desc',
        'quantity' : 20
                },
                {
        'name':'product4',
        'desc': 'random desc',
        'quantity' : 50
                },
                {
        'name':'product5',
        'desc': 'random desc',
        'quantity' : 50
                }
]

def get_unique_products(products):
    product_dict = {}

    for product in products:
        name = product['name']

        if name in product_dict:
            product_dict[name]['quantity'] += product['quantity']
        else:
            product_dict[name] = product

    return list(product_dict.values())

print(get_unique_products(product_list))