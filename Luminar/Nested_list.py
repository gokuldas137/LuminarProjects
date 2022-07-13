lst=[
    [10,11],
    [13,45],
    [50,15],
    [60,16],
    [70,60]
]

#print all numbers above 16

# for sub_ls in lst:
#     for num in sub_ls:
#         if num>16:
#             print(num)

flatten_list=[]
for sub_list in lst:
    for num in sub_list:
        flatten_list.append(num)

print(max(flatten_list))