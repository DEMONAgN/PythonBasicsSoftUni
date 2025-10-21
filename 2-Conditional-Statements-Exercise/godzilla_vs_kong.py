budget = float(input())
statists = int(input())
price_cloathing = float(input())

decor = budget * 0.10
total_clothes_price = price_cloathing * statists

if statists > 150:
    total_clothes_price *= 0.90

total_costs = decor + total_clothes_price

difference = abs(total_costs - budget)

if total_costs > budget:
    print(f"Not enough money!")
    print(f"Wingard needs {difference:.02f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {difference:.02f} leva left.")