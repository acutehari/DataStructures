arr=[5,5,7,8,8,9,9,10,10]
x=0
for i in range(1,len(arr)):
    if(arr[x]!=arr[i]): 
        x=x+1
        arr[x]=arr[i]

print(arr[:x+1])
    
