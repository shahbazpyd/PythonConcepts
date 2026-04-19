# n=123
# print("original:", n)
# reverse = 0
# while n > 0:
#     digit = n % 10
#     reverse = (reverse*10) + digit
#     n = n // 10
# print("reverse:", reverse)



# n = 121
# temp = n
# reverse = 0
# while n > 0:
#     digit = n %10
#     reverse = reverse*10 +digit
#     n = n//10
# if temp == reverse:
#     print("plindrom")
# else:
#     print("not Plindrom")


# n = 153
# temp = n
# digits = len(str(n))
# print("digits:", digits)
# sum = 0
# while n>0:
#     digit = n%10
#     sum = sum + digit**digits
#     print("sum:", sum)
#     n= n//10
# if sum == temp:
#     print("Armstrong")
# else:
#     print("not armstrong")


# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i
# print(fact)



# n = 10
# a = 0
# b = 1
# print(a, b, end=" ")
# for i in range(2, n+1):
#     c = a + b
#     print(c, end = " ")
#     a = b
#     b = c


# term = 10
# a = 0
# b = 1
# print(a, b, end = " ")
# while term > 2:
#     c = a + b
#     a = b
#     b = c
#     term = term -1
#     print(c, end= " ")


# n = 5
# if n <= 1:
#     print("not prime")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print("not prime")
#             break
#         else:
#             print("prime")
#             break
    
#     #         count +=1 
#     # if count>0:
#     #     print("not prime")
#     # else:
#     #     print("primt")

# def gcd(a, b):
#     # Repeat until remainder becomes 0
#     print("a:",a, "b:",b)
#     while b != 0:
#         a, b = b, a % b   # GCD Logic (Python-style formula)
#         print("a:",a, "b:",b)
#     return a

# # Example usage
# x = 80
# y = 60

# print("GCD is:", gcd(x, y))

# def gcd(a, b):
#     my_list = []
#     for i in range(1, a):
#         if a % i == 0:
#             if b % i == 0:
#                 my_list.append(i)
#     print("my list:", my_list)
#     return my_list.pop()  
# # Example usage
# x = 80
# y = 60

# print("GCD is:", gcd(x, y))




# def gcd(a, b):
#     # Find GCD using Euclidean algorithm
#     while b != 0:
#         a, b = b, a % b
#     print("GCD:", a)
#     return a

# def lcm(a, b):
#     # LCM Logic (Python-style formula)
#     return (a * b) // gcd(a, b)

# # Example usage
# x = 80
# y = 60

# print("LCM is:", lcm(x, y))


# def lcm(a, b):
#     my_list = []
#     # LCM Logic (Python-style formula)
#     for i in range(1 , 11):
#         mul1= a*i
#         mul2 = b*i
#         if mul1==mul2:
#             my_list.append(mul1)
#     print("my_list:", my_list)
#     return my_list[0]
        

# # Example usage
# x = 80
# y = 60

# print("LCM is:", lcm(x, y))


# n = 12345
# sum = 0
# while n>0:
#     sum = sum + n % 10
#     n = n // 10
# print("sum of digits:", sum)


def digital_root(n):
    # Repeat until number becomes a single digit
    while n >= 10:
        total = 0           # to store sum of digits

        # calculate sum of digits
        while n > 0:
            total += n % 10
            n //= 10

        # replace n with sum of digits
        n = total

    return n

# Example
num = int(input("Enter a number: "))
print("Digital root is:", digital_root(num))


# n = 12345
# sum = 0
# while n>0:
#     sum = sum + n % 10
#     n = n // 10

# print("sum of digits:", sum)