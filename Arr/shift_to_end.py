arr=[]
for i in range(10):
    arr.append(i)

#myList =list(range(1,10))
#print(myList)
print(arr)
pos = int(input("Který prvek chcete dostat na konec?"))
print(arr)
while (pos + 1) < len(arr): 
    arr[pos],arr[pos+1] = arr[pos+1], arr[pos]
    pos += 1
    print(arr)
    