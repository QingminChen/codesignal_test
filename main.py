# import collections
# def multi_password_strength_counter(passwords):
#     result_list = []
#     special_characters = "!@#$%^&*()-+"
#     for password in passwords:
#         tmp_dict = {}
#         if len(password) >= 8:
#             tmp_dict['length'] = True
#         else:
#             tmp_dict['length'] = False
#
#         if any(chr.isdigit() for chr in password):
#             tmp_dict['digit'] = True
#         else:
#             tmp_dict['digit'] = False
#
#         if any(chr.islower() for chr in password):
#             tmp_dict['lowercase'] = True
#         else:
#             tmp_dict['lowercase'] = False
#
#         if any(chr.isupper() for chr in password):
#             tmp_dict['uppercase'] = True
#         else:
#             tmp_dict['uppercase'] = False
#
#         for chr in password:
#             if chr not in special_characters:
#                 tmp_dict['special_char'] = False
#                 continue
#             else:
#                 tmp_dict['special_char'] = True
#                 break
#         result_list.append(tmp_dict)
#     return result_list
#     # implement this
#     pass
#
#
# passwords = ["password", "Pa$$w0rd", "SuperSecurePwd!", "weakpw"]
# results = multi_password_strength_counter(passwords)
# for result in results:
#     print(result)
#
# # The expected output is:
# # {'length': True, 'digit': False, 'lowercase': True, 'uppercase': False, 'special_char': False}
# # {'length': True, 'digit': True, 'lowercase': True, 'uppercase': True, 'special_char': True}
# # {'length': True, 'digit': False, 'lowercase': True, 'uppercase': True, 'special_char': True}
# # {'length': False, 'digit': False, 'lowercase': True, 'uppercase': False, 'special_char': False}
#
# # count_dict[element] = count_dict.get(element, 0) + 1   This is the good way to increment value on empty
#
#
# def keyword_index(docs):
#     index = {}
#     for doc_idx, doc in enumerate(docs):
#         for word in doc.split():
#             if word in index:
#                 index[word].append(doc_idx)
#             else:
#                 index[word] = [doc_idx]
#     return index
#
# def elect_board_member(votes):
#     count_dict = collections.defaultdict()
#     total_count = len(votes)
#     for vote in votes:
#         count_dict[vote] = count_dict.get(vote, 0)+1
#         if count_dict.get(vote) >= total_count/3:
#           return vote
#         else:
#           continue
#     return -1
#     # implement this
#     pass
#
# print(elect_board_member([1, 2, 3, 3, 3]))  # Expected output: 3
# print(elect_board_member([1, 2, 3, 4, 5]))  # Expected output: -1
# print(elect_board_member([1, 1, 1, 2, 2, 3, 3, 3]))  # Expected output: 1
#
#
#
# import collections
# def keyword_index(docs):
#     result_dict  = collections.defaultdict()
#     for doc_index, doc in enumerate(docs):
#         doc_words_list = doc.split(' ')
#         for word_index, word in enumerate(doc_words_list):
#             word_dict = result_dict.get(word,{})
#             word_dict[doc_index] = word_index+1
#             result_dict[word] = word_dict
#     return result_dict
#     # implement this
#     pass
#
# docs = ["Hello world", "world of python", "python is a snake"]
# print(keyword_index(docs))  # Expected output: {'Hello': {0: 1}, 'world': {0: 1, 1: 1}, 'of': {1: 1}, 'python': {1: 1, 2: 1}, 'is': {2: 1}, 'a': {2: 1}, 'snake': {2: 1}}


# def recursiveSumEven(arr, idx=0):
#     # sum = 0
#     # for idx, num in enumerate(arr):
#     #     if idx%2 == 0:
#     #         sum = sum+arr[idx]
#     # return sum
#     # implement this
#     if len(arr) == 0:
#         return 0
#     if idx < len(arr):
#        if idx != 0:
#           if idx%2 == 1 :
#              arr[idx]=arr[idx-1]+0
#           else:
#              arr[idx]=arr[idx-1]+arr[idx]
#        recursiveSumEven(arr,idx+1)
#     return arr[len(arr)-1]
#
#
# # Testing the function
# print(recursiveSumEven([1, 2, 3, 4, 5, 6])) # Expected output: 9
# print(recursiveSumEven([2, 3])) # Expected output: 2
# print(recursiveSumEven([]))
# print('123456')
#
#
# def factorial(num):
#     # implement this
#     if num == 0 :
#         return 1
#     if num < 0 :
#         return None
#     return num*factorial(num-1)
#     pass
#
# def factorials(nums):
#     return [factorial(num) if factorial(num) is not None else 'Error' for num in nums]
#
# # print(factorials([2, 3, 4])) # should print: [2, 6, 24]
# # print(factorials([1, 5, 6])) # should print: [1, 120, 720]
# print(factorials([0, -3, 10])) # should print: [1, 'Error', 3628800]


# # List of sorted ages in a social media platform
# ages = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
#
# def binary_search_iterative(data, target):  # this is the correct solution, my solution But now I think it doesn't make sense
#     low = 0
#     high = len(data)-1
#     while high - low > 0:
#         mid = (low + high) // 2
#         if target < data[mid]:
#             high = mid-1
#         elif target > data[mid]:
#             low = mid+1
#         else:  # if target is equal to data[mid]
#             return mid
#     return low if data[low] == target else None
#
# def binary_search_iterative2(data, target):  # this is the correct solution
#     low = 0
#     high = len(data)
#     while high - low >= 0:
#         mid = low + (high - low) // 2
#         if target < data[mid]:
#             high = mid-1
#         elif target > data[mid]:
#             low = mid+1
#         else:  # if target is equal to data[mid]
#             return mid
#     return None
#
# # Let's say we want to find out what position a 30-year-old holds in our sorted list of ages
# age_query = 30
# result = binary_search_iterative2(ages, age_query)
#
# if result is not None:
#     print(f"Age of {age_query} is found at position {result} in the age list.")
# else:
#     print(f"No profile is found with age {age_query}.")



# word_lengths = [i for i in range(1, 501)]  # Lengths from 1 to 500
#
# # TODO: Implement the recursion-based binary_search_recursive method
# def binary_search_recursive(data, target, low, high):
#     if low <= high:
#        mid = low + (high - low) // 2
#        if low <= high:
#           if data[mid] == target:
#              return mid
#           elif data[mid]<target:
#              return binary_search_recursive(data, target, mid+1, high)
#           else:
#              return binary_search_recursive(data, target, low, mid-1)
#     return None
#
#
# def binary_search(data, target, low, high): # This is the most make-sense solution
#     while low <= high:
#        mid = low + (high - low) // 2
#        if low <= high:
#           if data[mid] == target:
#              return mid
#           elif data[mid]<target:
#              low = mid + 1
#           else:
#              high = mid - 1
#     return -1
#
# # Suppose there is a spelling bee, and a contestant is given a word.
# # The contestant knows the word is in the dictionary, so let's find what position the length of this word would hold in our sorted list of word lengths
# word_length_query = 237
# result = binary_search_recursive(word_lengths, word_length_query, 0, len(word_lengths))
# # result = binary_search(word_lengths, word_length_query, 0, len(word_lengths))
# if result is not None:
#     print(f"Words of length {word_length_query} are found at position {result} in the word lengths list.")
# else:
#     print(f"No words are found with length {word_length_query}.")



# import math
#
# # Define the continuous function for the height of the ball at time t
# def h(t, initial_height, g):
#     return initial_height - (0.5) * g * t**2
#
# # Define the binary search function
# def binary_search(func, initial_height, g, target, left, right, precision):
#     while right - left > precision:
#         mid = left + (right - left) / 2  # we recommend calculate the mid in this way
#         if func(mid, initial_height, g) < target:
#             right = mid
#         else:
#             left = mid
#     return left + (right - left) / 2
#
# # Requested precision
# epsilon = 1e-6
# # Constants
# initial_height = 100  # Initial height in meters
# g = 9.81  # acceleration due to gravity
#
# # Time range
# time_range = [0, 10]
#
# # Call binary_search for h with the target being 0, indicating the hit of the ground
# result = binary_search(h, initial_height, g, 0, time_range[0], time_range[1], epsilon)
#
# print("Time when the ball hits the ground (seconds): ", result)
#
#
# # The value of x for which f(x) is approximately 0 within the interval [-5, 5] is:  1.923944428563118  1.9239446520805359


import math
# this is not a classic problem ,which has no generic solution to solve it,
# since different equations have special cases, you need to based on the equation to think out the loop condition is by your own brain which is not efficient
# way to solve this kind of problem
# it's not linear sorted problem
import numpy as np


# Define a continuous function 'f' where f(x) = x^4 - x^2 - 10
def f(x):
    return x ** 4 - x ** 2 - 10


# Define the binary search function
def binary_search(func, target, left, right, precision):
    while func(left) > target and func(right) > target:
        middle = left + (right -left) / 2
        if func(middle) < target+precision:
            left = middle
        else:
            right = middle

    return left + (right -left) / 2


epsilon = 1e-6  # to make sure the solution is within an acceptable range
target = 50  # target value for root of function 'f'
start = -5  # starting point of the interval
end = 5  # ending point of the interval

# def range_with_floats(start, stop, step):
#     while stop > start:
#         yield start
#         start += step
#
# for x in range_with_floats(-5,5.1,0.15):
#    print(str(x)+' '+str(f(x)))


result = binary_search(f, target, start, end, epsilon)
print("The value of x for which f(x) is approximately 50 within the interval [" + str(start) + ", " + str(end) + "] is: ",result)