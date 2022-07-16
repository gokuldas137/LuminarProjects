# f=open("abs.txt")
# lst=[]
# for view in f:
#    lst.append(view)
# print(lst)


         # OR
#
# f=open("abs.txt")
# view=list(f)
# print(view)

f=open("abs.txt")
out=[line.rstrip("\n") for line in f]        #strip method is used to remove
print(out)