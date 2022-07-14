# print most recursive element

pattern="ABACCDA"

a={}
word_count={"a":2,"b":5,"c":2,"d":4,"e":2}

wc_list=word_count.items()
print(sorted(wc_list,key=lambda item:item[1],reverse=True))     #sorting in dictionary

#max()

print(max(wc_list,key=lambda item:item[1]))