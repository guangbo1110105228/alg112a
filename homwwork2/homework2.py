# 方法 1
def power2n_1(n):
    return 2**n
print(power2n_1(5))

# 方法 2a：用遞迴
def power2n_2a(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2

    return power2n_2a(n-1)+power2n_2a(n-1)
print(power2n_1(5))

# 方法2b：用遞迴
def power2n_2b(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2

    return 2*power2n_2b(n-1)
print(power2n_1(5))

# 方法 3：用遞迴+查表
fib = [None]*10000
fib[0] = 0
fib[1] = 2

def power2n_3(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    elif fib[n]:
        return fib[n]
    else:
        fib[n] = power2n_3(n-1)+power2n_3(n-1)
        return fib[n]
print(power2n_1(5))

