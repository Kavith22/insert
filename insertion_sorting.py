num=[5,4,3,2,1]
for i in range(1,len(num)):
    key=num[i]
    j=i-1
    while key<num[j] and j>=0:
        num[j+1]=num[j]
        j=j-1
    num[j+1]=key
    print(num)