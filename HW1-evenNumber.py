n = int(input("Input one digit integer number: "))
if n<10 :
    for i in range(int(n)+1):
        if i%2==0:
            print(i)        
else:
    print("Number is not one digit.")



    
