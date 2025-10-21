annual_tax = int(input())

basketball_shoes = annual_tax - (annual_tax * 0.40)
basketball_clothes = basketball_shoes - (basketball_shoes * 0.20)
basketball_balls = basketball_clothes / 4
basketball_accessories = basketball_balls / 5
equipment_price = annual_tax + basketball_shoes + basketball_clothes + basketball_balls + basketball_accessories

print(equipment_price)