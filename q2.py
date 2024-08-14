number = range(1,10)

previousnum = 0

for currentnum in number:
    sum = currentnum + previousnum

print(f"current number: {currentnum}, Previousnumber:{previousnum}, sum:{sum}")
previousnum = currentnum