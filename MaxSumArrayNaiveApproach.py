arr=[3,8,2,5,7,6,12]
maxx=float('-inf')
window=4
for i in range(len(arr)-window+1):
    current=0
    for j in range(i,i+window):
        current=current+arr[j]
    maxx=max(current,maxx)
print(maxx)