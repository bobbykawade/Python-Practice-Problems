a=[1,2,3]
b=['a','b','c']
c=[]
def li(li1,li2):
    for i in range(len(li1)):
        c.append(li1[i])
        c.append(li2[i])
        
    return c

print(li(a,b))