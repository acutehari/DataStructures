arr=[3,8,2,5,7,6,12]
current=0
window=4
for i in range(window):
    current=current+arr[i]
maxx=current
for i in range(1,len(arr)-window+1):
    current=current-arr[i-1]+arr[i+window-1]
    if(current>maxx):
        maxx=current
print(maxx)