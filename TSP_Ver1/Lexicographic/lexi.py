def perm(order):
    largestI = -1
    for i in range(0,len(order)-1):
        if order[i] < order[i+1]:
            largestI = i
    if largestI == -1:
        return False
    largestJ = 0
    for j in range(0,len(order)):
        if order[largestI] < order[j]:
            largestJ = j
    Swap(order, largestI, largestJ)
    tempArr = order[largestI+1:]
    tempArr = tempArr[::-1]
    InsertArray(order, tempArr, largestI+1)
    print(order)
    return True
    
def Swap(x, i, j):
    temp = x[i]   
    x[i] = x[j]
    x[j] = temp
    
def InsertArray(order, tempArr, largestJ):
  for i in range(0, len(tempArr)):
    order[largestJ+i] = tempArr[i]
    
a = [1,2,3]
print(a)
counter = 0
while(perm(a)):
  perm(a)
  counter += 2 
print (counter)