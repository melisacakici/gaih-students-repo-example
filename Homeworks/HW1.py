# Python homework 1

#Question 1 : creating a list and swap half of the list with other half

list = [1,2,3,4,5,6,7,8]
l = len(list)
m=l//2
list[:m],list[m:] = list[m:],list[:m] 
print(list)

#Question 2: 

n = input("Please input an one digit integer variable: ")

for i in range(int(n)):
    if i%2==0:
        print(i)
