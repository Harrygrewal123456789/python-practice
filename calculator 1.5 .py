a=float(input('enter the first number: '))
b=float(input('enter the second number: '))
print(''' If you want to perform addition write 1
If you want to perform Subtraction write 2
If you want to perform multiplication write 3
If you want to perform division write 4''')
c=int(input("write the number of function you want to perform "))
if c==1 :
    print("the sum is", a+b)
elif c==2  :
    print("the difference is",a-b)
elif c==3 :
    print('the multiplication is ', a*b) 
elif c==4 :
    if b!=0 :
        print('the division is', a/b)
    else :
        print('Error:division by 0 is not allowed')
else :
    print("Invalid Choice . Enter the number between 1 and 4")
     
    