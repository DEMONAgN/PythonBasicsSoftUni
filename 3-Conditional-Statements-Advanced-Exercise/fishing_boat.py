group_budget = int(input())
season = input()
count_of_fishers = int(input())

rent = 0

if season == 'Spring':
    rent = 3000
elif season == 'Summer' or season == 'Autumn':
    rent = 4200
elif season == 'Winter':
    rent = 2600

if count_of_fishers <=6:
    rent *= 0.90
elif 7 <= count_of_fishers <=11:
    rent *= 0.85
else:
    rent *= 0.75

if count_of_fishers % 2 == 0 and season != 'Autumn':
    rent *= 0.95

difference = abs(group_budget - rent)

if group_budget >= rent:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")