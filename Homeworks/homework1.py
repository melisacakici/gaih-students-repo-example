list = [1,2,3,4,5,6,7,8]
l = len(list)
m=l//2
list[:m],list[m:] = list[m:],list[:m] 
print(list)

