# # # data = [("Alice", 85), ("Bob", 90), ("Alice", 95), ("Bob", 80)]

# # # totals = {}              # dict
# # # counts = {}              # dict
# # # students = set()         # set

# # # # Step 1: Process data
# # # for name, marks in data:   # tuple unpacking
# # #     students.add(name)
    
# # #     totals[name] = totals.get(name, 0) + marks
# # #     counts[name] = counts.get(name, 0) + 1

# # # # Step 2: Calculate averages
# # # result = []               # list
# # # for name in students:
# # #     avg = totals[name] / counts[name]
# # #     result.append((name, avg))   # tuple

# # # print(result) 

# # orders = [
# #     ("user1", "apple"),
# #     ("user2", "banana"),
# #     ("user1", "apple"),
# #     ("user2", "orange"),
# # ]

# # result = {}          # dict
# # products = set()     # set

# # for user, product in orders:
# #     products.add(product)
    
# #     if user not in result:
# #         result[user] = {}
    
# #     result[user][product] = result[user].get(product, 0) + 1

# # print(result)


# sentence = "this is a test this is only a test"

# words = sentence.split()   # list
# freq = {}                  # dict

# # Count frequency
# for word in words:
#     freq[word] = freq.get(word, 0) + 1

# # Find duplicates
# duplicates = []            # list
# for word, count in freq.items():
#     if count > 1:
#         duplicates.append((word, count))  # tuple

# print(duplicates)


# 4. 📊 Employee Department Mapping

# Given:

# employees = [
#     ("Alice", "HR"),
#     ("Bob", "IT"),
#     ("Charlie", "HR"),
#     ("David", "IT"),
# ]
# Task:
# Create dict: department → list of employees
# Use set to find unique departments
# Return:
# {
#   "HR": ["Alice", "Charlie"],
#   "IT": ["Bob", "David"]
# }

# employees = [
#     ("Alice", "HR"),
#     ("Bob", "IT"),
#     ("Charlie", "HR"),
#     ("David", "IT"),
# ]

# dept_map = {}        # dict
# departments = set()  # set

# for name, dept in employees:
#     departments.add(dept)
    
#     if dept not in dept_map:
#         dept_map[dept] = []
    
#     dept_map[dept].append(name)

# print(dept_map)




# nums = [2, 7, 11, 15, 2, 7]
# target = 9

# seen = {}        # dict
# pairs = set()    # set

# for num in nums:
#     complement = target - num
    
#     if complement in seen:
#         pairs.add(tuple(sorted((num, complement))))  # tuple
    
#     seen[num] = True

# result = list(pairs)  # list
# print(result)



# person1 = ["Mon", "Tue", "Wed"]
# person2 = ["Wed", "Thu", "Fri"]

# set1 = set(person1)
# set2 = set(person2)

# common = set1 & set2   # set intersection

# result = [(day,) for day in sorted(common)]  # list of tuples

# print(result)



# inventory = [
#     ("apple", 10),
#     ("banana", 5),
#     ("apple", 5),
# ]

# stock = {}       # dict
# items = set()    # set

# for item, qty in inventory:
#     items.add(item)
#     stock[item] = stock.get(item, 0) + qty

# result = [(item, stock[item]) for item in items]  # list of tuples

# print(result)



# words = ["eat", "tea", "tan", "ate", "nat", "bat"]

# anagrams = {}    # dict

# for word in words:
#     key = tuple(sorted(word))   # tuple
    
#     if key not in anagrams:
#         anagrams[key] = []
    
#     anagrams[key].append(word)

# print(anagrams)
# =======================================================

# data = [("Alice", 85), ("Bob", 90), ("Alice", 95), ("Bob", 80)]

# marks_dict = {}

# # Step 1: Collect marks
# for name, marks in data:
#     if name not in marks_dict:
#         marks_dict[name] = []
#     marks_dict[name].append(marks)
# print(marks_dict)

# # Step 2: Calculate average
# result = []
# for name in marks_dict:
#     print(name)
#     avg = sum(marks_dict[name]) / len(marks_dict[name])
#     result.append((name, avg))

# print(result)


# orders = [
#     ("user1", "apple"),
#     ("user2", "banana"),
#     ("user1", "apple"),
#     ("user2", "orange"),
# ]

# result = {}

# for user, product in orders:
#     if user not in result:
#         result[user] = {}
    
#     if product not in result[user]:
#         result[user][product] = 0
    
#     result[user][product] += 1

# print(result)



sentence = "this is a test this is only a test"
words = sentence.split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

result = []

for word, count in freq.items():
    if count > 1:
        result.append((word, count))

print(result) 