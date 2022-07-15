# expenses=[12000,13000,140000,15000,16000]
#
# # # 1st approach for iteration(with indexes)
# for i in range(0,5):
#     print(expenses[i])
#
#
# # 2nd approach for iteration
# for amount in expenses:
#     print(amount)

# # 3rd approach for iteration
# for i in range(0,len(expenses)):
#      print(expenses[i])


# eg:

# names=["c++","c","javascript","java","python"]
#
# print(len(names))
#
# for i in range(0,5):
#     print(names[i])
#
# for name in names:
#     print(name)
#
# list.append("html")


# even numbers

# numbers=[12,13,14,15,16,17,18]
# for num in numbers:
#      if num%2==0:
#           print(num)
#


# print num+1 if num >15 else print num-1  , if num==15 print num=15

# numbers=[12,13,14,15,16,17,18]
# for num in numbers:
#      if num>15:
#           print(num+1)
#      elif num==15:
#           print(num)
#      else:
#           print(num-1)
#


# print count of numbers where numbers in range of 14-18

# count=0
# numbers = [12, 13, 14, 15, 16, 17, 18]
# for num in numbers:
#      if 14<=num<=18:
#           count+=1
# print(count)

#      OR

# count=0
# numbers = [12, 13, 14, 15, 16, 17, 18]
# for num in range(14,19):
#      count+=1
# print(count)


# find count of pos,neg,zero count

# p_count=0
# n_count=0
# z_count=0
# numbers=[-1,2,3,-4,-6,0,0,0,-6,4,5,-7,8,9,0]
# for num in numbers:
#      if num>0:
#           p_count+=1
#      elif num==0:
#           n_count+=1
#      else:
#           z_count=+1
# print("Positive count ",p_count," Negative count ",n_count," Zeros count ",z_count)


# sum of list

# sum=0
# numbers=[-1,2,3,-4,-6,0,0,0,-6,4,5,-7,8,9,0]
#
# for num in numbers:
#      sum+=num
# print(sum)


#       OR


# numbers=[-1,2,3,-4,-6,0,0,0,-6,4,5,-7,8,9,0]
# print(sum(numbers))


# find count of pos,neg,zero count and their sums

p_count = 0
n_count = 0
z_count = 0
numbers = [-1, 2, 3, -4, -6, 0, 0, 0, -6, 4, 5, -7, 8, 9, 0]
for n in numbers:
    if n > 0:
        p_count += n
    elif n < 0:
        n_count += n
    elif n == 0:
        z_count += n
print("Positive sum ", p_count, " Negative sum ", n_count, " Zero sum ", z_count)
