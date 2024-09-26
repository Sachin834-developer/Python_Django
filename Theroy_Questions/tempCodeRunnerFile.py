def decorater_func(func):
    def wrapper_func(*args,**kwargs):
        print(*args)# here it accepts the params that are passed to the original function .
        result = func(*args,**kwargs)
        print(result)# after executong original function 
        #if result.islower():
        return result.upper()
    return wrapper_func

@decorater_func
def display(name):
    return name

res = display('sachin')
print(res)