lst = [
    [10, 11],
    [13, 45],
    [50, 15],
    [60, 16],
    [70, 60]
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


odd=[num for num in flatten_lst if num%2!=0]
print(odd)

even=[num for num in flatten_lst if num%2==0]   #filter
print(sum(even))

mappedlist=[num+1 if num>25 else num-1 for num in flatten_lst] #mapped list
print(mappedlist)