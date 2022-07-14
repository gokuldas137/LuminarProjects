# print first recursive element

pattern = "ABACCDA"

charcount={}
recchar=[]
for char in pattern:
    if char in charcount:
        recchar.append(char)

    else:
        charcount[char]=1
print("First rec is ",recchar[0])
print("Second rec is ", recchar[1])

#                 OR

# shifna maam method

# pattern = "ABAACCDA"
# rec = " "  # AC
# patt = " "  # ABC
# for p in pattern:
#     if p not in patt:
#         patt += p
#     else:
#         rec += p
# print("first recursive element is", rec[1], " , Second recursive element is", rec[2])
# print(rec)
# ........



# ...........
# char_count = {}
# for char in pattern:
#     if char in char_count:
#         print("First recursive element is", char)
#         break
#     else:
#         char_count[char] = 1
# print(char_count)