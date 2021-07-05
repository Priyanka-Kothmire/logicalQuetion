list= [1,2,3,1,2,2]
l=[]
i=0
while i<len(list):
    a=list[i]
    if a not in l:
        l.append(a)
    i=i+1
print(l)


