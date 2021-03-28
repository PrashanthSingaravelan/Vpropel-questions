def isBallShuffled(list1,list2):
    element=index=flag=0
    
    for i in range(len(list1)):
        if list1[i]==list2[0]:
            element = list1[i]
            index = i
    j=index
    
    for i in range(len(list1)):
        j = j%len(list1)
        if (list1[j]!=list2[i]):
            flag = 1
            return flag
        else:
            j+=1
            
    return flag


n = int(input())
list1 = [input()for i in range(n)]
list2 = [input()for i in range(n)]

if (isBallShuffled(list1,list2)==0):
    print("Not Shuffled")
else:
	print("Shuffled")
