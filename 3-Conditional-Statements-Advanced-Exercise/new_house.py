flower_type = input()
count_of_flowers = int(input())
budget = int(input())
flower_price = 0

if flower_type == "Roses":
    flower_price = 5 * count_of_flowers
    if count_of_flowers > 80:
        flower_price *= 0.90

elif flower_type == "Dahlias":
    flower_price = 3.80 * count_of_flowers
    if count_of_flowers > 90:
        flower_price *= 0.85

elif flower_type == "Tulips":
    flower_price = 2.80 * count_of_flowers
    if count_of_flowers > 80:
        flower_price *= 0.85

elif flower_type == "Narcissus":
    flower_price = 3 * count_of_flowers
    if count_of_flowers < 120:
        flower_price += flower_price * 0.15

elif flower_type == "Gladiolus":
    flower_price = 2.50 * count_of_flowers
    if count_of_flowers < 80:
        flower_price += flower_price * 0.20

difference = abs(budget - flower_price)

if budget >= flower_price:
    print(f"Hey, you have a great garden with {count_of_flowers} {flower_type}"
          f" and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")