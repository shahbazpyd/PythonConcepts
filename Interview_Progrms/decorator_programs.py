# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         result = func()
#         print(result)

#     return wrapper

# @timer
# def slow_task():
#     time.sleep(2)
#     return "done"

# slow_task()



# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         # print(f"{func.__name__} took {start:.2f} {end:.2f} seconds")
#         print(f"{func.__name__} took {end - start:.2f} seconds")
#         return result

#     return wrapper

# @timer
# def slow_task():
#     time.sleep(2)
#     return "done"

# slow_task()

# def sum_of_three(func):
#     def wrapper(*args, **kwargs):
#         print("args",args)
#         print("kwargs",kwargs)
#         a,b= args
#         args = a+10, b+10
#         print("args:", args)
#         result = func(*args, **kwargs)
#         # sum= 10 + result
#         # return sum
#         return result
#     return wrapper
    
# @sum_of_three
# def sum(a,b):
#     c = a+b
#     return c

# result = sum(5,5)
# print(result)

# @make_loud
# def greet():
#     return "hello"

# def make_loud(func):
#     print(func)
#     print(func())

# make_loud(greet)

# def make_loud(func):
#     def wrapper():
#         result = func()
#         return result.upper()
#     return wrapper

# @make_loud
# def greet():
#     return "hello"

# # louder = make_loud(greet)
# print(greet())
# # greet = make_loud(greet)
# # print(greet())

def sumdecorator(func):
    def wrapper(*args, **kwargs):

        try:
            num=int(input("enter third number"))
        except ValueError:
            print("Error: That's not a valid number!")
            num=0
    
        result=func(*args, **kwargs)
        return num+result

    return wrapper
    
    
@sumdecorator
def sum(a, b):
    return a+b

result = sum(5,10)
print(result)