results = [
    {"district": "tvm", "win": 98, "A+": 45000},
    {"district": "ktm", "win": 95, "A+": 44000},
    {"district": "apy", "win": 97, "A+": 47000},
    {"district": "idk", "win": 90, "A+": 38000},
    {"district": "ekm", "win": 99, "A+": 56000},
    {"district": "pta", "win": 99, "A+": 58000},
    {"district": "tsr", "win": 98, "A+": 57000},
    {"district": "kzd", "win": 99, "A+": 58000},
    {"district": "pkd", "win": 95, "A+": 50000},
    {"district": "mpm", "win": 90, "A+": 45000},

]

# #sort results based on win percentage-- desc order
#
# print(sorted(results,key=lambda res:res["win"],reverse=True))
#
# #print dist with min win %
# print(min(results,key=lambda i:i["win"]))
#
# #sort results based on A+
# print(sorted(results,key=lambda i:i["A+"], reverse=True))
#
# #print dist with low A+
# print(sorted(results,key=lambda i:i["A+"]))

#total students who got A+
aplus=[i["A+"] for i in results]
print(aplus)
print(sum(aplus))