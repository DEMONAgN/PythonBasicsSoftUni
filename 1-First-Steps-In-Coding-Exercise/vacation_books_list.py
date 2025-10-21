pages = int(input())
pages_per_hour = int(input())
days = int(input())

total_time = pages // pages_per_hour
hours_need_per_book = total_time // days
print(hours_need_per_book)