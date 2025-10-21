import math

record_time = float(input())
meters = float(input())
time_in_meters = float(input())

has_to_swim = meters * time_in_meters
water_resistance = math.floor(meters / 15) * 12.5

total_time = has_to_swim + water_resistance

difference = abs(total_time - record_time)
if total_time >= record_time:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
