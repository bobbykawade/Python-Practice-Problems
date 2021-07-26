a=[]

for i in range(7):
    inpu=int(input("Enter no"))
    a.append(inpu)

def maa(li):
    outp=0
    for i in range(len(a)):
        outp=outp+a[i]
    return outp

print(maa(a))