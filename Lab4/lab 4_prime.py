n=int(input('enter a number : '))
if n>1:
    for i in range(2, n/2):
        if (n%i) == 0:
            print('the number is not prime')
        else:
            print('the number is prime')
else:
            print('the number is prime')


    
