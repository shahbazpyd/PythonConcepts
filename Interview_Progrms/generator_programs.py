# def get_numbers():
#     numbers = []
#     for i in range(10):
#         numbers.append(i)
#     return numbers

# nums = get_numbers()
# print(nums)


# def get_numbers():
#     for i in range(10):
#         yield i
# nums = get_numbers()
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))


# def even_numbers(limit):
#     # your code here
#     for i in range(0, limit+1):
#         if i % 2 == 0:
#             yield i


# for n in even_numbers(10):
#     print(n)

# Expected output:
# 0
# 2
# 4
# 6
# 8
# 10




def my_func(list):
    for i in list:
        yield i
    # return list

list = [1,2,3,4,5]
result= my_func(list)
print(next(result))
print(next(result))
print(next(result))