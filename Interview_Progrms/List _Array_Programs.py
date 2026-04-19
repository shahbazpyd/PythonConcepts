# # nums = list(map(int, input("enter number: ").split()))
# nums = list(map(int, input("Enter numbers: ").split(',')))
# print(nums)

# largest = nums[0]
# smallest = nums[0]
# for num in nums:
#     if num > largest:
#         largest = num
#     if num < smallest:
#         smallest = num
# print("largest:", largest)
# print("smallest:", smallest)


# # Start

# # Take a list of numbers as input
# numbers = list(map(int, input("Enter numbers: ").split()))

# # Assume the first element as both largest and smallest
# largest = numbers[0]
# smallest = numbers[0]

# # Compare each element with current largest and smallest
# for element in numbers:
#     # Update largest if a bigger value is found
#     largest = max(largest, element)

#     # Update smallest if a smaller value is found
#     smallest = min(smallest, element)

# # Display largest and smallest elements
# print("Largest element:", largest)
# print("Smallest element:", smallest)

# # Stop




# # numbers = list(map(int, input("Enter numbers: ").split()))
# values = list(map(int, input("enter you values:").split()))
# print("original value: ", values)
# unique_element = []
# for i in values:
#     if i not in unique_element:
#         unique_element.append(i)
# print("after remove duplicate:", unique_element)



# values = list(map(int, input("enter you values:").split()))
# reversed_list = []
# length = len(values) -1
# for i in range(length, -1, -1):
#     reversed_list.append(values[i])
# print("reversed list:", reversed_list)

# # Start

# # Take a list as input
# numbers = list(map(int, input("Enter elements: ").split()))

# # Create an empty list to store reversed elements
# reversed_list = []

# # Read elements from the end of the list
# for i in range(len(numbers) - 1, -1, -1):
#     element = numbers[i]

#     # Add each element to the new list
#     reversed_list = reversed_list + [element]

# # Display the reversed list
# print("Reversed list:", reversed_list)

# # Stop



# numbers = list(map(int, input("Enter elements: ").split()))
# largest = 0
# second_largest = 0
# for element in numbers:
#     if element > largest:
#         second_largest= largest
#         largest = element

#     elif element > second_largest and element != largest:
#         second_largest = element
# print("second largest: ", second_largest)

# Start

# # Take a list of numbers as input
# numbers = list(map(int, input("Enter numbers: ").split()))

# # Initialize largest and second largest
# largest = second_largest = float('-inf')
# print(largest, second_largest)

# # Compare each element
# for element in numbers:
#     # If element is greater than largest
#     if element > largest:
#         second_largest = largest
#         largest = element

#     # If element is between largest and second largest
#     elif element > second_largest and element != largest:
#         second_largest = element

# # Display the second largest number
# if second_largest == float('-inf'):
#     print("Second largest element does not exist")
# else:
#     print("Second largest element:", second_largest)

# # Stop



# numbers = list(map(int, input("Enter elements: ").split()))
# is_sorted = True
# for i in range(len(numbers)-1):
#     current = numbers[i]
#     next_element = numbers[i +1]

#     if current > next_element:
#         is_sorted = False
#         break
# if is_sorted:
#     print("List is sorted")
# else:
#     print("List is not sorted")



# numbers = list(map(int, input("Enter elements: ").split()))
# sum = 0
# for num in numbers:
#     sum+=num
# print("sum of all element:", sum)



# numbers1 = list(map(int, input("Enter elements: ").split()))
# numbers2 = list(map(int, input("Enter elements: ").split()))

# merged = []
# for i in numbers1:
#     merged.append(i)
# for i in numbers2:
#     merged.append(i)
# print("merged list:", merged)

# # Start

# # Take first list as input
# list1 = list(map(int, input("Enter elements of first list: ").split()))

# # Take second list as input
# list2 = list(map(int, input("Enter elements of second list: ").split()))

# # Create a new empty list
# merged_list = []

# # Add all elements of the first list
# for element in list1:
#     merged_list.append(element)

# # Add all elements of the second list
# for element in list2:
#     merged_list.append(element)

# # Display the merged list
# print("Merged list:", merged_list)

# Stop




# numbers1 = list(map(int, input("Enter elements: ").split()))
# numbers2 = list(map(int, input("Enter elements: ").split()))
# common_list = []
# for element in numbers1:
#     if element in numbers2:
#         common_list.append(element)
# print("common element in both lists:", common_list)


# # Start

# # Take first list as input
# list1 = list(map(int, input("Enter elements of first list: ").split()))

# # Take second list as input
# list2 = list(map(int, input("Enter elements of second list: ").split()))

# # Create an empty list to store common elements
# common_elements = []

# # Read each element from the first list
# for element in list1:
#     # Check if it exists in the second list
#     if element in list2:
#         # Add element to common list
#         common_elements.append(element)

# # Display common elements
# print("Common elements:", common_elements)

# # Stop


# Start

# Take a list as input
# numbers = list(map(int, input("Enter elements: ").split()))
# print("numbers", numbers)

# # Take number of positions to rotate
# k = int(input("Enter number of positions to rotate: "))
# print("k1", k)

# # Handle rotation greater than list length
# k = k % len(numbers)
# print("k", k)


# # Separate and arrange elements in rotated order
# rotated_list = numbers[k:] + numbers[:k]

# # Display rotated list
# print("Rotated list:", rotated_list)

# Stop




# numbers = list(map(int, input("Enter elements: ").split()))
# even_count = 0
# odd_count = 0
# for element in numbers:
#     if element % 2 == 0:
#         even_count+=1
#     else:
#         odd_count+=1
# print("all even:", even_count)
# print("all odd: ", odd_count)

# # Start

# # Take a list of numbers as input
# numbers = list(map(int, input("Enter numbers: ").split()))

# # Initialize even and odd counts
# even_count = 0
# odd_count = 0

# # Read each element from the list
# for element in numbers:
#     # Check if element is divisible by 2
#     if element % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1

# # Display even and odd counts
# print("Even count:", even_count)
# print("Odd count:", odd_count)

# # Stop




# sentence = "python is very easy language and python is most popular language"
# words = sentence.split()
# print(words)
# freq = {}
# for word in words:
#     if word not in freq:
#         freq[word] = 1
#     else:
#         freq[word] = freq.get(word,0)+1
# print("frequency of words: ", freq)

# # Start

# # Take a sentence as input
# sentence = input("Enter a sentence: ")

# # Convert the sentence into individual words
# words = sentence.split()

# # Create an empty dictionary to store word counts
# freq = {}

# # Read each word one by one
# for word in words:
#     # Increase count if word exists, else set count to 1
#     freq[word] = freq.get(word, 0) + 1

# # Display the word frequency dictionary
# print("Word frequency:", freq)

# # Stop


# words = {'python': 2, 'is': 2, 'very': 1, 'easy': 1, 'language': 2, 'and': 1, 'most': 1, 'popular': 1}
# sorted_word = {}
# for word, value in words:



# # Start

# # Take a dictionary as input
# data = {
#     'apple': 5,
#     'banana': 2,
#     'cherry': 8,
#     'date': 3
# }
# print("data", data)
# # Convert dictionary items into key-value pairs
# items = data.items()
# print("items", items)

# # Sort the items based on values
# sorted_items = sorted(items, key=lambda item: item[1])
# print("sorted_items", sorted_items)

# # Store the sorted result in a new dictionary
# sorted_dict = dict(sorted_items)

# # Display the sorted dictionary
# print("Sorted dictionary by value:", sorted_dict)

# # Stop



# dict1 = {
#     'apple': 5,
#     'banana': 2,
#     'cherry': 8,
#     'date': 3
# }
# dict2 = {
#     'apple': 4,
#     'mango': 3,
#     'orange': 7,
#     'date': 5
# }
# merged = {}
# for key, value in dict1.items():
#     merged[key]= value
# for key, value in dict2.items():
#     merged[key]= value

# print("merged dict:", merged)

# # Start

# # Take two dictionaries as input
# dict1 = {
#     'a': 10,
#     'b': 20,
#     'c': 30
# }

# dict2 = {
#     'b': 200,
#     'd': 40
# }

# # Create a new empty dictionary
# merged_dict = {}

# # Add all key-value pairs from the first dictionary
# for key, value in dict1.items():
#     merged_dict[key] = value

# # Add all key-value pairs from the second dictionary
# # (updates value if key already exists)
# for key, value in dict2.items():
#     merged_dict[key] = value

# # Display the merged dictionary
# print("Merged dictionary:", merged_dict)

# # Stop




# Start

# Take a dictionary as input
# data = {
#     'apple': 50,
#     'banana': 30,
#     'cherry': 80,
#     'date': 60
# }

# # Assume the first key has the maximum value
# max_key = next(iter(data))

# max_value = data[max_key]

# print("max_key", max_key)
# print("max_value", max_value)
# # Compare values of all keys
# for key in data:
#     if data[key] > max_value:
#         max_value = data[key]
#         max_key = key

# # Display the key with the highest value
# print("Key with maximum value:", max_key)

# Stop


# max_key = max(data, key=data.get)
# print("Key with maximum value:", max_key)





# data = {
#     'apple': 50,
#     'banana': 30,
#     'cherry': 80,
#     'date': 60
# }

# key = input("enter your key")
# if key in data:
#     print("Key exist")
# else:
#     print("key not present")




# data = {
#     'apple': 50,
#     'banana': 30,
#     'cherry': 80,
#     'date': 60
# }
# key = input("enter your key to remove")
# if key in data:
#     removed_key = data.pop(key)
#     print("removed successfully")
#     print("updated data: ", data)
# else:
#     print("entered key is not available")




# data = {
#     'apple': 50,
#     'banana': 30,
#     'cherry': 80,
#     'date': 60
# }

# inverted = {}
# for key, value in data.items():
#     inverted[value] = key

# print("inverted data: ", inverted)