arr=[1,2,3,5,7,10,11,15]
#array should be always sorted to use two pointer technique
left=0
right=len(arr)-1
target=15
while(left<right):
    current_sum=arr[left]+arr[right]

    if(current_sum==target):
        print("pair found:",arr[left]+arr[right])
        break
    elif(current_sum<target):
        left+=1
    else:
        right-=1





