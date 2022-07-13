mobiles = [
    [1000, "samsungA52", "4g", "AMOLED", 27000, "samsung", 12],
    [1001, "samsungA52s", "5g", "AMOLED", 32000, "samsung", 20],  # 18th video
    [1002, "redminote10", "4g", "led", 17000, "redmi", 50],
    [1003, "redminote11pro", "5g", "superAMOLED", 20000, "redmi", 70],
    [1004, "samsungA72", "5g", "AMOLED", 27000, "samsung", 1],
    [1005, "samsungA53", "5g", "AMOLED", 27000, "samsung", 34],
    [1006, "samsungA52", "5g", "AMOLED", 27000, "samsung", 7],
    [1007, "samsungA53", "5g", "AMOLED", 27000, "samsung", 89],
    [1008, "samsungA22", "5g", "AMOLED", 27000, "samsung", 0],
    [1009, "iphone13", "5g", "AMOLED", 97000, "apple", 0],
    [1010, "oneplusnordce2", "5g", "AMOLED", 23000, "oneplus", 67],
]
# # 1.Total number of mobiles
# print(f"Total number of mobiles{len(mobiles)}")


# # q1 - total no: of out of stock mobiles
# outofstock=[mob for mob in mobiles if mob[-1]==0]
# print(outofstock)



# # q2 - total no of out of stock
# print("No of out of stock ",len(outofstock))


# # total stock
# totalstock=[mob[-1] for mob in mobiles]  #mapping
# print("total stock ",sum(totalstock))



# # q3 - print mobiles available in range 20K to 30K
# pricerange=[mob for mob in mobiles if mob[4] in range(20000,30000)]
# print("between ",pricerange)



# # q4 - print all 5G phones
# mobs=[mob for mob in mobiles if mob[2]=="5g"]
# print("5g ",mobs)
#
# # q5 - print samsung mobiles
# mobs=[mob for mob in mobiles if mob[-2]=="samsung"]
# print(mobs)



# # q6 - print costly mobile
# max_prices=max([mob[4] for mob in mobiles])
# costly=[mob for mob in mobiles if mob[4]==max_prices]
# print("\n costly",costly)
#

# q7 - print low cost mobile
# low_cost=min(mobiles,key=lambda m:m[4])
# print(low_cost)
#
#
# # q8 - print all mobiles having stock > 10
#  mobiles=[mob for mob in mobiles if mob[-1]>10]
# print(mobs)
#
#
# # q9 - count of mobiles having display amoled
#
# count=[mob for mob in mobiles if mob[3]=="AMOLED"]
# print(len(count))
#
#
# # # q10 - sort mobiles based on price order by ascending
# mobiles.sort(reverse=False,key=lambda m:m[4])
# print(mobiles)

#
# q11 - sort mobiles based on avl stock order by descending
# (mobiles.sort(reverse=True,key=lambda m:m[-1]))
# print(mobiles)


# q13 - most available stock
# avl_stck=max(mobiles,key=lambda m:m[-1])
# print(avl_stck)


# q14 - least available stock
# avl_stckmin=min(mobiles,key=lambda m:m[-1])
# print(avl_stckmin)


# sort
# mobiles.sort(reverse=True,key=lambda m:m[4])
# print(mobiles)



# is there any mobile available at rs 10000
mobten=[mob[4]==10000 for mob in mobiles]
print("available" if True in mobten else "no")