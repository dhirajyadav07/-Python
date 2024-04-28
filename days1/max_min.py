lst=[2,5,3,8,67,4,34,12]     #given list 
max=min=lst[0]
for i in range(len(lst)):
    if lst[i]>max:
        max=lst[i]
    if lst[i]<min:
        min=lst[i]

print("maximum :",max)
print("minimum :",min)

