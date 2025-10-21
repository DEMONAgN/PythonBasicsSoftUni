price_pens = 5.80
price_markers = 7.20
price_cleaning_per_liter = 1.20

pen_pack = int(input())
marker_pack = int(input())
liters = int(input())
percent = int(input()) / 100

total_price_without_discout = (pen_pack * price_pens) \
                                  + (marker_pack * price_markers) \
                                  + (liters * price_cleaning_per_liter)

total_price_with_discount = total_price_without_discout - (total_price_without_discout * percent)

print(total_price_with_discount)