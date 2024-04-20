# pa=principal amount ,A=total amount t=time ,r=rate 
pa=int(input("Enter the amount: "))
r=int(input("Enter the rate :"))
t=int(input("Enter the time :"))
rate_decimal=r/100
A=pa*(1+rate_decimal)**t
print(A," is the total amount")