square_meters_for_landscraping = float(input())
price_for_landscraping_the_whole_yard = square_meters_for_landscraping * 7.61

discount = price_for_landscraping_the_whole_yard * 0.18

total_price = price_for_landscraping_the_whole_yard - discount

print(f"The final price is: {total_price} lv.")
print(f"The discount is: {discount} lv.")