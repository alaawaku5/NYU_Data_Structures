# def remove_all(lst, value):
#     start = ""
#     for i in range(len(lst)):
#         if start != "" and lst[i] != value:
#             lst[start], lst[i] = lst[i], lst[start]
#             if lst[start+1] == value:
#                 start += 1
#             else:
#                 start = i
#         if start == "" and lst[i] == value:
#             start = i
#
#     for i in range(len(lst)-start):
#         lst.pop()
#
#     return lst
#
lst = [2,1,2,3,2,5]
print(lst*2)
