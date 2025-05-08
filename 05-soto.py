print("-- Program start")
print("Table codes:  A = add, S = subtract, M = multiple, D = divide")

table_code = input("Select table code: ").upper()
number = float(input("Enter number for table: "))

if table_code == "A":
    print("Add")
    for i in range(1, 11):
        print(f"{number + i:.1f} = {number:.1f} + {i}")
elif table_code == "S":
    print("Subtract")
    for i in range(1, 11):
        print(f"{number - i:.1f} = {number:.1f} - {i}")
elif table_code == "M":
    print("Multiply")
    for i in range(1, 11):
        print(f"{number * i:.1f} = {number:.1f} * {i}")
elif table_code == "D":
    print("Divide")
    for i in range(1, 11):
        if i != 0:
            print(f"{number / i:.1f} = {number:.1f} / {i}")
else:
    print("Invalid table code")

print("---done :D")
