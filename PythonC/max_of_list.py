a=[10,20,304,50,40,50,20]
def max_of_list(li):
    ma=0
    for i in a:
        if ma <= i:
            ma=i
               
    return ma
print(max_of_list(a))