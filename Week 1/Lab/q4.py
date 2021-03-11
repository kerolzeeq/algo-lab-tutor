num = eval(input('Enter a number: '))
divisor = num
list = []

for divisor in range(divisor, 0, -1):
    if num!=1:
        if num%divisor==0:
            list.append(divisor)
print(list)