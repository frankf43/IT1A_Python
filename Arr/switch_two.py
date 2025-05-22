arr=[]
for i in range(10):
    arr.append(i)

print(arr)

while True:
    a = int(input("Který prvek bude první, který chcete vyměnit?"))
    b = int(input("Který prvek bude druhý, který chcete vyměnit?"))
    
    if a!=b and a > 0 and b > 0 and a < len(arr) and b < len(arr):
        break

pom = arr[a]
arr[a] = arr[b]
arr[b] = pom

#arr[1], arr[5] = arr[5], arr[1]
print(arr)