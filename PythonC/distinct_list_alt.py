a=[1,2,3,4,5,6,7,8,9]
b=['a','b','c']
c=[]

def li(li1,li2):
    ca=0
    cb=0
    for i in range(len(li1)):
        ca = ca+1
    for i in range(len(li2)):
        cb = cb+1
    if ca>cb:
        lent = ca
    else:
        lent = cb
    print(lent)
    for i in range(lent):
        if i < ca:
            c.append(li1[i])
        if i <cb:
            c.append(li2[i])
        
        
    return c

print(li(a,b))