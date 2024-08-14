mylist = ['apple','banana','mango','grapes','apple','banana']

elementcount = {}

for element in mylist:
    if element in elementcount:
        elementcount[element] +=1
    else:
        elementcount[element] =1
print(elementcount)