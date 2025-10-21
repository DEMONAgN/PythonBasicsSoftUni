deposit_amount = float(input())
deposit_term = int(input())
anual_percent = float(input()) / 100
amount = deposit_amount + deposit_term * ((deposit_amount * anual_percent) / 12)
print(amount)