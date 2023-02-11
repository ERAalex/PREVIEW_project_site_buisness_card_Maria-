
n = int(input())
week = 1
total_eaten = 0

check = True

while check:
    if n > total_eaten:
        total_eaten = 3**week
        week += 1
    else:
        check = False
        print(week)
