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


def recursiveSumEven(arr, idx=0):
    # sum = 0
    # for idx, num in enumerate(arr):
    #     if idx%2 == 0:
    #         sum = sum+arr[idx]
    # return sum
    # implement this
    if len(arr) == 0:
        return 0
    if idx < len(arr):
       if idx != 0:
          if idx%2 == 1 :
             arr[idx]=arr[idx-1]+0
          else:
             arr[idx]=arr[idx-1]+arr[idx]
       recursiveSumEven(arr,idx+1)
    return arr[len(arr)-1]


# Testing the function
print(recursiveSumEven([1, 2, 3, 4, 5, 6])) # Expected output: 9
print(recursiveSumEven([2, 3])) # Expected output: 2
print(recursiveSumEven([]))
print('123456')


def factorial(num):
    # implement this
    if num == 0 :
        return 1
    if num < 0 :
        return None
    return num*factorial(num-1)
    pass

def factorials(nums):
    return [factorial(num) if factorial(num) is not None else 'Error' for num in nums]

# print(factorials([2, 3, 4])) # should print: [2, 6, 24]
# print(factorials([1, 5, 6])) # should print: [1, 120, 720]
print(factorials([0, -3, 10])) # should print: [1, 'Error', 3628800]