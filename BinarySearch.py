#binary search alwasy should be in sorted array
loc=-1
arr=[24,36,39,47,78,87,92,112,156]
item=90
B=0
E=len(arr)-1

while B<=E:
    mid=(B+E)//2
    if item==arr[mid]:
        loc=mid
        print(loc)
        break
    elif item>arr[mid]:
        B=mid+1
    else:
        E=mid-1

print(loc)
