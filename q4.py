def firstandlast(numbers):
    if len(numbers) < 1:
        return False
    return numbers[0] == numbers[-1]

numbers = [10,20,30,40,50,60,10]
print(firstandlast(numbers))