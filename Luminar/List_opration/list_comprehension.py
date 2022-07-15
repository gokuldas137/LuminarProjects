# lst = [
#     [10, 11],
#     [13, 45],
#     [50, 15],
#     [60, 16]
# ]
#
# flatten_list=[num for sub_lst in lst for num in sub_lst ]
# print(flatten_list)




# print numbers in the list greater than 16

# lst = [
#     [10, 11],
#     [13, 45],
#     [50, 15],
#     [60, 16]
# ]
# flatten_list=[num for sub_lst in lst for num in sub_lst ]
# nums_greater_16=[num for num in flatten_list if num>16]
# print(nums_greater_16)




# print odd numbers from flatten_list

# lst = [
#     [10, 11],
#     [13, 45],
#     [50, 15],
#     [60, 16]
# ]
# flatten_list=[num for sub_list in lst for num in sub_list]
# odd_numbers=[num for num in flatten_list if num%2!=0]
# print(odd_numbers)
#
#

# print sum of even numbers
#
# lst = [
#     [10, 11],
#     [13, 45],
#     [50, 15],
#     [60, 16],
#     [70, 60]
# ]
#
# flatten_lst=[num for sub_lst in lst for num in sub_lst]       # Filtered list case
# even_nums=[num for num in flatten_lst if num%2==0]            # (because here we just want to filter the numbers into a new list)
# print(sum(even_nums))
#


# print into a single list if num>25 num+1 else num-1


lst = [                                                # Remember if it is filter case, put if else at last
    [10, 11],                                          # and for mapped case put if else in the begining
    [13, 45],
    [50, 15],
    [60, 16],
    [70, 60]
]
flatten_lst=[num for sub_lst in lst for num in sub_lst]               # Mapped case
new_lst=[num+1 if num>25 else num-1 for num in flatten_lst]           # (called mapped because we want to make changes to the elements
print(new_lst)                                                        # into a new list)