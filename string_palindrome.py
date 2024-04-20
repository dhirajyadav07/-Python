str=input("Enter a string : ")
len_str=len(str)

for i in range(int(len_str/2)):
    if str[i]==str[len_str-1-i]:
        flag=1
    else:
        flag=0
if flag==1:
    print(str," is a palindrome string ")
else:
    print(str," is not a palindrome string ")

# using string reversal 
if str == str[::-1]:
    print(str," is a palindrome string ")
else:
    print(str," is not a palindrome string ")
