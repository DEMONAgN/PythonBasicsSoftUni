type_projection = input()
rows = int(input())
columns = int(input())
capacity = rows * columns
income = 0

if type_projection == "Premiere":
    income = capacity * 12.00
elif type_projection == "Normal":
    income = capacity * 7.50
elif type_projection == "Discount":
    income = capacity * 5

print(f"{income:.2f}")