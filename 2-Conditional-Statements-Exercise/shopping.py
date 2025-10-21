budget = float(input())
videocards = int(input())
processors = int(input())
rams = int(input())

videocard_price = 250 * videocards
processor_price = 0.35 * videocard_price
ram_price = 0.10 * videocard_price

shopping = videocard_price + (processor_price * processors) + (ram_price * rams)

if videocards > processors:
    shopping *= 0.85

difference = abs(budget - shopping)

if budget >= shopping:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")