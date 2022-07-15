mobiles = [
    [1000, "samsungA52", "4g", "AMOLED", 27000, "samsung", 12],
    [1001, "samsungA52s", "5g", "AMOLED", 32000, "samsung", 20],                                  # 18th video
    [1002, "redminote10", "4g", "led", 17000, "redmi", 50],
    [1003, "redminote11pro", "5g", "superAMOLED", 20000, "redmi", 70],
    [1004, "samsungA72", "5g", "AMOLED", 27000, "samsung", 1],
    [1005, "samsungA53", "5g", "AMOLED", 27000, "samsung", 34],
    [1006, "samsungA52", "5g", "AMOLED", 27000, "samsung",7],
    [1007, "samsungA53", "5g", "AMOLED", 27000, "samsung",89],
    [1008, "samsungA22", "5g", "AMOLED", 27000, "samsung",0],
    [1009, "iphone13", "5g", "AMOLED", 97000, "apple",0],
    [1010, "oneplusnordce2", "5g", "AMOLED", 23000, "oneplus",67],
]


# q - number of mobiles ?

# print("Total number of mobiles =",len(mobiles))

# q1 - total no: of out of stock mobiles
#
# mobs=[mob for mob in mobiles if mob[-1]==0]
# print(len(mobs))

# q2 - total stock

# mobs=[mob[-1] for mob in mobiles ]
# print(sum(mobs))

# q3 - print mobiles available in range 20K to 30K
#
# mobs=[mob for mob in mobiles if 20000<= mob[4] <=30000]
# print(mobs)

#      OR

# mobs=[mob for mob in mobiles if mob[4] in range(20000,30001)]
# print(mobs)


# q4 - print all 5G phones

# mobs=[mob for mob in mobiles if mob[2]=="5g"]
# print(mobs)

# q5 - print samsung mobiles

# mobs=[mob for mob in mobiles if mob[-2]=="samsung"]
# print(mobs)

# q6 - print costly mobile

# mobs=max([mob[4] for mob in mobiles])
# costly_pro=[mob for mob in mobiles if mob[4]==mobs]
# print(costly_pro)

#      OR

# costly_mob=max(mobiles,key=lambda m:m[4])
# print(costly_mob)




# q7 - print low cost mobile

# mobs=min([mob[-3] for mob in mobiles])
# low_cost=[mob for mob in mobiles if mob[-3]==mobs]
# print(low_cost)

#        OR

# low_cost=min(mobiles,key=lambda m:m[4])
# print(low_cost)


# q8 - print all mobiles having stock > 10

# mobiles=[mob for mob in mobiles if mob[-1]>10]
# print(mobs)


# q9 - count of mobiles having display amoled

# count=[mob for mob in mobiles if mob[3]=="AMOLED"]
# print(len(count))


# q10 - sort mobiles based on price order by descending

# mobiles.sort(reverse=True,key=lambda m:m[4])
# print(mobiles)

# q11 - sort mobiles based on avl stock order by descending

avl_stck=(mobiles.sort(reverse=True,key=lambda m:m[-1]))
print(mobiles)
# q12 - is there any mobiles available at rs 10000 ?

mobs=[mob[4]==10000 for mob in mobiles ]
print("Available" if True in mobs else "Not Available")                            # 18th video

# q13 - most available stock

# avl_stck=max(mobiles,key=lambda m:m[-1])
# print(avl_stck)

# q14 - least available stock

# least_stck=min(mobiles, key=lambda m:m[-1])
# print(least_stck)

# q15 -


