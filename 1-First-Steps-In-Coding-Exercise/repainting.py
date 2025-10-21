qty_nylon = int(input())
qty_paint = int(input())
qty_thinner = int(input())
hours_needed_for_workers = int(input())

price_nylon = 1.50
price_paint = 14.50
price_thinner = 5.00
price_bags = 0.40
#extra materials
total_paint = qty_paint + (qty_paint * 0.10)
total_nylon = qty_nylon + 2

total_material_cost = ((total_nylon * price_nylon) + (total_paint * price_paint) +
                       (price_thinner * qty_thinner) + price_bags)

amount_with_workers = (total_material_cost * 0.30) * hours_needed_for_workers

print(amount_with_workers + total_material_cost)