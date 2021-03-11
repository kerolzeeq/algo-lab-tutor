num = eval(input('Enter value of n : '))

def fibonacci(n):
    fibonacci_list = [0, 1]
    for i in range(1, n-1, 1):
        fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i])
    return fibonacci_list

print(fibonacci(num))