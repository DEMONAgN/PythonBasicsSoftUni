city = input()
stocks = float(input())
percent = -1

if city == "Sofia":
    if 0 <= stocks <= 500:
        percent = 0.05
    elif 500 < stocks <= 1000:
        percent = 0.07
    elif 1000 < stocks <= 10000:
        percent = 0.08
    elif stocks > 10000:
        percent = 0.12
elif city == "Varna":
    if 0 <= stocks <= 500:
        percent = 0.045
    elif 500 < stocks <= 1000:
        percent = 0.075
    elif 1000 < stocks <= 10000:
        percent = 0.10
    elif stocks > 10000:
        percent = 0.13
elif city == "Plovdiv":
    if 0 <= stocks <= 500:
        percent = 0.055
    elif 500 < stocks <= 1000:
        percent = 0.08
    elif 1000 < stocks <= 10000:
        percent = 0.12
    elif stocks > 10000:
        percent = 0.145

if percent >= 0:
    total_sales = percent * stocks
    print(f"{total_sales:.2f}")
else:
    print("error")