num = eval(input('Enter a number: '))
divisor = num - 1
flag = True

for divisor in range(divisor, 1, -1):
    if num!=1:
        if num%divisor==0:
            flag = False

if flag==True and num>1:
    print(f'{num} is a prime number')
else:
    print(f'{num} is NOT a prime number')