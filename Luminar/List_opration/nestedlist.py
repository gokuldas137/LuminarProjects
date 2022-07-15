lst = [
    [10, 11],
    [13, 45],
    [50, 15],
    [60, 16]
]

# for sub_lst in lst:
#     for num in sub_lst:
#         if num>16:
#             print(num)
#
#
# print(max(lst))       # this is not accurate

# to print the max value from the above nested list


flatten_lst = []
for sub_lst in lst:
    for num in sub_lst:
        flatten_lst.append(num)
print(max(flatten_lst))
