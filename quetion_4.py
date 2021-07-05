a=[1,2,3,4,5]
b=[10,20,30,40,50]
i=0
while i<len(a):
    j=1
    while j<=len(b):
        print(a[i],b[-i])
        i+=1
        j+=1