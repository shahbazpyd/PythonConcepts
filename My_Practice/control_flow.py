# """
# *
# **
# ***
# *****
# """

# for i in range(5):
#     for j in range(i):
#         print("*", end = "")
#     print()


# for i in range(5):
#     for j in range(5):
#         if j<=i:
#             print("*", end= "")
#     print()

# size = 5
# for i in range(size + 1):
#     print("*" * i)

# """
#     *
#    **
#   ***
# *****
# """
# n=5
# for i in range(5):
#     for j in range(5):
#         if j >=n-1:
#             print("*",end = "")
#         else:
#             print(" ", end = "")
#     n-=1
#     print()


# size = 5
# for i in range(size, 0, -1): # Counting backwards from 5 to 1
#     print(" " * (size - i) + "*" * i)


# size = 5
# for i in range(1, size + 1):
#     # (size - i) calculates spaces, (i) calculates stars
#     print(" " * (size - i) + "*" * i)




# count of given digit if input is 9767 then output is 29
# algorithm
# step 1 - extract one from given count_digit
# step 2 - store and add in varaiable
# step 3 - repeat step 1 and 2 untill the number will be ess than 0

def count_digit(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total
num = 9767
count = count_digit(num)
print("count of digit", count)