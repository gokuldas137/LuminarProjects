# lst=[2,3,4,6]                          # Linear search (Less efficient because iteration is more)
# sum=8
# dup_list=[]
# for i in range(0,len(lst)):
#     for j in range(i+1,len(lst)):
#        current_sum=lst[i]+lst[j]
#        if current_sum==sum:
#            print("Pairs are ",lst[i],",",lst[j])
#            break


# Big 0 - Denotes the amount of complexity




# lst=[2,3,4,6]                             # 15th video
# element=7
# lst.sort()                       # more efficient because iteration is less
# low=0
# upp=len(lst)-1
# while(low<upp):
#     current_sum=lst[low]+lst[upp]
#     if current_sum==element:
#         print("Pairs are",lst[low], lst[upp])
#         break
#     elif current_sum>element:
#         upp-=1
#     elif current_sum<element:
#         low+=1
#
#



lst=[2,3,4,6,5]                             # 15th video                # Algorithm
element=7
lst.sort()                       # more efficient because iteration is less
low=0
upp=len(lst)-1
while(low<upp):
    current_sum=lst[low]+lst[upp]
    if current_sum==element:
        print("Pairs are",lst[low], lst[upp])
        low+=1
    elif current_sum>element:
        upp-=1
    elif current_sum<element:
        low+=1
