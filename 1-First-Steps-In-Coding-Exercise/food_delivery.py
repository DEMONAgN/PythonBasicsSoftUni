chicken_menu_price = 10.35
fish_menu_price = 12.40
vegan_menu_price = 8.15
delivery = 2.50

qty_chicken_menus = int(input())
qty_fish_menus = int(input())
qty_vegan_menus = int(input())

menu_prices = ((qty_chicken_menus * chicken_menu_price) + (qty_fish_menus * fish_menu_price) +
               (qty_vegan_menus * vegan_menu_price))
desert = menu_prices * 0.20

total_order_price = menu_prices + desert + delivery
print(total_order_price)