a=open("students.txt")
all_std=[std.rstrip("\n") for std in a]

b=open("failed.txt")
failed=[std.rstrip("\n") for std in b]

c=open("passedstd.txt","w")

passed=set(all_std)-set(failed)
print(passed)

for st in passed:
    st+="\n"
    c.write(st)