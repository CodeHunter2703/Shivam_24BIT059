n=int(input('enter a number : '))
total=0
while(n>0):
    digit=n%10
    total=total+digit
    n=n//10
print('the sum of digits is : ',total)
