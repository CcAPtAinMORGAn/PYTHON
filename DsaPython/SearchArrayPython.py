list=[1,2,5,6]

k=int(input("Enter value to search in array"))

for i in range (0,4):
    if(list[i]==k):
        print("Value is at index" ,i)