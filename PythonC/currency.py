def indian_curr(s):
    if len(s)<= 3:
        return s
    else:
        s=s[::-1]
        t=s[:3]
        t=t+','
        c=0
        for i in range(3,len(s)):
            t=t+s[i]
            c=c+1
            if c==2:
                t=t+','
                c=0
        if len(s)%2!=0:
            t=t[:-1]
        return t[::-1]

s = input("500000:")
print(indian_curr(s))