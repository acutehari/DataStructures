old_array=[5,5,7,8,8,9,9,10,10]
new_array=old_array
new_array[0]=old_array[0]
x=0
for i in range(1,len(old_array)):
    if(new_array[i]!=old_array[x]):
        x+=1
        new_array[x]=old_array[i]

print(new_array[:x+1])
