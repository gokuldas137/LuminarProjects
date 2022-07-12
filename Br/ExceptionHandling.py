b = 0
try:
    a = 10 / b
    print(a)
    print("Try completed")
except ZeroDivisionError:
    print("division by zero not possible")
print("Prgoram completed")
