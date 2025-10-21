excursion_price = float(input())
qty_puzzle = int(input())
qty_doll = int(input())
qty_bear = int(input())
qty_minion = int(input())
qty_truck = int(input())

puzzle_price = 2.60
doll_price = 3
bear_price = 4.10
minion_price = 8.20
truck_price = 2

total_price = ((qty_puzzle * puzzle_price) +
               (qty_doll * doll_price) +
               (qty_bear * bear_price)+
               (qty_minion * minion_price) +
               (qty_truck * truck_price))

total_toys_qty = qty_puzzle + qty_doll + qty_bear + qty_minion + qty_truck

if total_toys_qty >= 50:
    total_price *= 0.75

rent = total_price * 0.10
profit = total_price - rent

difference = abs(profit - excursion_price)

if profit >= excursion_price:
    print(f'Yes! {difference:.2f} lv left.')
else:
    print(f'Not enough money! {difference:.2f} lv needed.')