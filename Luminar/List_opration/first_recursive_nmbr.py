# print first recursive number


lst1 = [10, 11, 11, 12, 13, 14, 14, 14]
dup_list = []
for i in range(0, len(lst1)):
    for j in range((i + 1), len(lst1)):
        if lst1[i] == lst1[j]:
            dup_list.append(lst1[i])

print(dup_list)
print("Most frequent element is", dup_list[1], "\n", "first recursive element is ", dup_list[0],
      "Second recursive element is ", dup_list[1])

# print(dir(list))        # list all operations of list at the ending
