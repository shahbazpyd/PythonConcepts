# str = "shahbaz"
# reversed = ""
# index = len(str) -1
# while index >= 0:
#     reversed = reversed + str[index]
#     index = index -1
# print(str, reversed)



# str = "rabar"
# reversed = ""
# index = len(str) -1
# while index >= 0:
#     reversed = reversed + str[index]
#     index = index -1
# if str == reversed:
#     print("plindron")
# else:
#     print("not plindrome")



# str = "rabar"
# reversed = ""
# index = len(str) -1
# vowels = 0
# consonents = 0
# while index >= 0:
#     char = str[index]
#     index = index -1
#     if char in "aeiouAEIOU":
#         vowels = vowels + 1
#     else:
#         consonents = consonents + 1
# print("vowels:", vowels)
# print("consonents:", consonents)

# str = "rabar"
# reversed = ""
# index = len(str) -1
# vowels = 0
# consonents = 0
# for char in str:
#     if char in "aeiouAEIOU":
#         vowels += 1
#     else:
#         consonents += 1
# print("vowels:", vowels)
# print("consonents:", consonents)


# str1 = "S hah Baz"
# str2 = "sha Hba z"

# str1 = str1.replace(" ", "")
# str2 = str2.replace(" ", "")

# str1 = str1.lower()
# str2 = str2.lower()

# sort_str1 = sorted(str1)
# sort_str2 = sorted(str2)

# if sort_str1 == sort_str2:
#     print("anagram")
# else:
#     print("not anagram")


# str1 = "S hah Baz"
# str2 = "sha Hba z"

# if sorted(str1.replace(" ", "").lower()) == sorted(str2.replace(" ", "").lower()):
#     print("anagram")
# else:
#     print("Not anagram")


# str = "shahbaz"
# result = ""
# for char in str:
#     if char not in result:
#         result = result + char
# print(result)



# str = "shahbaz"
# freq = {}
# for char in str:
#     if char in freq:
#         freq[char] = freq.get(char, 0) + 1 
#     else:
#         freq[char] = 1

# print(freq)



# str = "shashbaz"
# freq = {}
# for char in str:
#     if char in freq:
#         freq[char] = freq.get(char, 0) + 1 
#     else:
#         freq[char] = 1

# for char, value in freq.items():
#     if freq[char] == 1:
#         print(char, value)
#         break
#     else:
#         print("no such charector")

# str = "shahabzs"
# freq = {}
# found = False
# for char in str:
#     if char in freq:
#         freq[char] = freq.get(char, 0) + 1 
#     else:
#         freq[char] = 1
# for char in str:
#     if freq[char] == 1:
#         print(char)
#         found = True
#         break
# if not found:
#     print("not found")
        
    


# def capatilize_first(sentence):
#     words = sentence.split()
#     for word in words:
#         print(word.title(), end = " ")
        
# sentence = "Python is very easy language."
# capatilize_first(sentence)


# # Start

# # Take a sentence as input
# sentence = input("Enter a sentence: ")

# # Split the sentence into words
# words = sentence.split()

# # Convert the first letter of each word to uppercase
# capitalized_words = []
# for word in words:
#     capitalized_words.append(word.capitalize())

# # Join all words back into a sentence
# result = " ".join(capitalized_words)

# # Display the modified sentence
# print("Modified sentence:", result)

# # Stop




# word = input("enter your word")
# if word.isdigit():
#     print("Contain only digit")
# else:
#     print("Contain other character")



# # Take input
# s = input("Enter a string: ")

# all_digits = True

# for ch in s:
#     if ch < '0' or ch > '9':
#         all_digits = False
#         break

# if all_digits:
#     print("All characters are digits")
# else:
#     print("Not all characters are digits")


# s = input("Enter a string: ")

# if all(ch.isdigit() for ch in s):
#     print("contain only digit")
# else:
#     print("not contain only digit")


            
sentence = input("Enter your sentence")
words = sentence.split()
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word
print("longest:", longest)          
            
        
    

    