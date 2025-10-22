month = input()
nights_of_staying= int(input())

price_per_night_studio = 0
price_per_night_apartment = 0

if month == "May" or month == "October":
    price_per_night_studio = 50
    price_per_night_apartment = 65
    if nights_of_staying > 14:
        price_per_night_studio *= 0.70
        price_per_night_apartment *= 0.90
    elif nights_of_staying > 7:
        price_per_night_studio *= 0.95

elif month == "June" or month == "September":
    price_per_night_studio = 75.20
    price_per_night_apartment = 68.70
    if nights_of_staying > 14:
        price_per_night_studio *= 0.80
        price_per_night_apartment *= 0.90

elif month == "July" or month == "August":
    price_per_night_studio = 76
    price_per_night_apartment = 77
    if nights_of_staying > 14:
        price_per_night_apartment *= 0.90

total_price_for_studio = price_per_night_studio * nights_of_staying
total_price_for_apartment = price_per_night_apartment * nights_of_staying

print(f"Apartment: {total_price_for_apartment:.2f} lv.")
print(f"Studio: {total_price_for_studio:.2f} lv.")