array=[25,16,38,10,35,48,20,50]
max1=array[0]
max2=array[1]
if(array[0]>array[1]):
    max1=array[0]
    max2=array[1]
else:
    max1=array[1]
    max2=array[0]
for i in range(2,len(array)):
    if(array[i]>max1):
            max2=max1
            max1=array[i]
    elif(array[i]>max2):
            max2=array[i]

print(max2)