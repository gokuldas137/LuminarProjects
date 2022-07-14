# print unique elements from the list

# lst=[10,10,1,12,13,14,15,16,16,16]
# st=set(lst)
# print(st)
#
# print(dir(st))

# operations on sets

# st1={1,2,3,4,5}
# st2={10,11,12,2,3}
# union_set=st1.union(st2)
# print(union_set)
#
# intersection_set=st1.intersection(st2)
# print(intersection_set)
#
# diff_set=st1.difference(st2)
# print(diff_set)


# print the failed students from the lists

students = ["ram", "ravi", "hari", "tom", "tom", "nikhil", "jain", "john"]
passed = ["ravi", "hari", "tom"]

st = set(students)
ps = set(passed)
failed = st.difference(ps)
print(failed)

#      OR

failed = set(students).difference(set(passed))
print(failed)
