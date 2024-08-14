def reverse(list):
    chunksize = len(list)
    chunks = [list[i:i + chunksize] for i in range(0,len(list),chunksize)]
    reversedchunks = [chunk[::-1] for chunk in chunks]
    return reversedchunks

list = [10,20,30,40,50,60]
answer = reverse(list)
print(answer)