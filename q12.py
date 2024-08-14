numbers = [10,20,30,40,50,60,78,41,52,63,98,120,175]

for num in numbers:
    if num > 150:
        break
    if num % 5 == 0:
        print(num)