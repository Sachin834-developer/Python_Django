# Exceptions MCQ
# once exception handled no need handle it again in the main code.
def sub_func(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print('NameError in sub_func')
    finally:
        print('finally in subfunc')

try:
    sub_func(5,0)
except ZeroDivisionError:
    print('NameError in Main code')
finally:
    print('finally in main code')