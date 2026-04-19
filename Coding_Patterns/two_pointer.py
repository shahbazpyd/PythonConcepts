# # brute force
# from unittest import result


# def pair_sum_bruteforce(arr, target):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] + arr[j] == target:
#                 return True
#     return False

# def pair_sum(arr, target):
#     left = 0
#     right = len(arr) - 1

#     while left < right:
#         pairlist= []
#         current_sum = arr[left] + arr[right]
#         if current_sum==target:
#             pairlist.append(left)
#             pairlist.append(right)
#             return pairlist
#         elif current_sum < target:
#             left += 1
#         else:
#             right -= 1
#     return "There is no such pairs"

# arr = [2,3,4,7,8,9]
# target = 19

# # result = pair_sum_bruteforce(arr, target)
# result = pair_sum(arr, target)
# print(result)




# def reverse_string(s):
#     return s[::-1]


# def reverse_string(s):
#     s= list(s)
#     left = 0
#     right = len(s) -1 

#     while left < right:
#         s[left], s[right] = s[right], s[left]
#         left += 1
#         right -= 1
#         print(s)

#     return ''.join(s)
# s= "shahbaz"
# result = reverse_string(s)
# print(result)

# name= "shahbaz"
# list= list(name)
# list = ''.join(list)
# print(list)





# def is_palindrome(s):
#     return s == s[::-1]

def is_palindrome(s):
    left = 0
    right =len(s)-1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True
s= "121"
result = is_palindrome(s)
print(result)
