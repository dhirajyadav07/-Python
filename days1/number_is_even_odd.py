num=int(input("Enter the number : "))
print("using bitwise and operator we identify the given number is odd or even")
if num & 1 == 0 :
    print("%d is even"%num)
else:
    print("%d is odd"%num)
