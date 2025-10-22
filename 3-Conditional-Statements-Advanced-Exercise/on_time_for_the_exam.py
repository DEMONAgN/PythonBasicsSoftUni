hour_of_exam = int(input())
minute_of_exam = int(input())
hour_of_coming_exam = int(input())
minute_of_coming_exam = int(input())

exam_time = hour_of_exam * 60 + minute_of_exam
arrival_time = hour_of_coming_exam * 60 + minute_of_coming_exam

difference = arrival_time - exam_time

if difference > 0:
    print("Late")
    hours = difference // 60
    minutes = difference % 60

    if difference < 60:
        print(f"{minutes} minutes after the start")
    else:
        print(f"{hours}:{minutes:02d} hours after the start")

elif difference == 0:
    print ("On time")

elif difference < 0:
    if abs(difference) <= 30:
        print("On time")
        print(f"{abs(difference)} minutes before the start")
    else:
        print("Early")
        hours = abs(difference) // 60
        minutes = abs(difference) % 60

        if abs(difference) < 60:
            print(f"{minutes} minutes before the start")
        else:
            print(f"{hours}:{minutes:02d} hours before the start")