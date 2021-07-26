def mergedivide(alist):
    if len(alist) <= 1:
        return alist
    else:
        mid = int(len(alist)//2)
        leftli = alist[:mid]
        rightli = alist[mid:]
        sorted_left = mergedivide(leftli)
        sorted_right = mergedivide(rightli)
        return merge_sort(sorted_left,sorted_right)
def merge_sort(li1,li2):
    ans = []
    len1 = len(li1)
    len2 = len(li2)
    i = j = 0
    while i < len1 or j < len2:
        if i<len1 and j < len2:
            if(li1[i]<li2[j]):
                ans.append(li1[i])
                i += 1
            else:
                ans.append(li2[j])
                j += 1
        elif i<len1:
            ans.append(li1[i])
            i +=1
        elif j<len2:
            ans.append(li2[j])
            j +=1
    return ans





alist = [45,12,21,23,55,65,14,11,9]
print(mergedivide(alist))
