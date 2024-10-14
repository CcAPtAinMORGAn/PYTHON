list = [1,1,1,4,5,5,8,9,8,5,4]
printed = []

for i in range(len(list)):
    if list[i] not in printed:
        counter=0
        for j in range (i+1,len(list)):
            if(list[i]==list[j]):
                counter+=1
                print(list[i],"",end='')
                printed.append(list[i])
                break
            if(list[i]!=list[j] and counter<1):
                print(list[i],"",end='')
                printed.append(list[i])
                break
            print(list[i],"",end='')