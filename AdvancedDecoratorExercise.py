input = eval(input("enter the 3 numbers to be added"))

def decorator_set(fn):
    def wrapper(*args,**kwargs):
        print(f"you have called the function named {fn.__name__}{args}")
        result = fn(args[0],args[1],args[2])
        print(f"your result is {result}")
    return wrapper

@decorator_set
def add(a,b,c):
    return a+b+c

add(input[0],input[1],input[2])
# print(f"the result is{a}")