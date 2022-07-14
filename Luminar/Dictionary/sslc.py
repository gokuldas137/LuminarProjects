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

# sort result based on win order by desc

print(sorted(results,key=lambda res:res["win"],reverse=True))

# print dist with min win %

print(min(results,key=lambda res:res["win"]))

# sort results based on A+ desc

print(sorted(results,key=lambda res:res["A+"],reverse=True))

# print dist with low count A+

print(min(results,key=lambda res:res["A+"]))

# print total number of students who got full A+

aplus=[res["A+"]for res in results ]                              # list comprehension
print(sum(aplus))


