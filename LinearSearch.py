loc=-1
arr=[29,75,69,22,2,95]
item=29

for i in range(0,len(arr)) :
    if arr[i]==item:
        loc=i
        print(loc)
        break

print(loc)