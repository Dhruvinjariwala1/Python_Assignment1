def productofsum(x,y):
    product = x * y
    if product > 1000:
        return x + y
    else:
        return product
answer = productofsum(20,70)
print(answer)