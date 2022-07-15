frameworks = [
    ["django", "python", 4],
    ["flask", "python", 3],
    ["spring", "java", 5],
    ["express", "javascript", 4],
    ["angular", "typescript", 4]

]

# print frameworks that uses python

pythn=[py for py in frameworks if py[1]=="python"]
print(pythn)

# print languages having rating > 3

rating=[fw for fw in frameworks if fw[-1]>3]
print(rating)
