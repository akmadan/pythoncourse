d = 3  # global variable
def func(a,b):
    c = 10   # local variable

    global e
    e = 4

    return a+b+c+d+e

def func2(m,n):
    return m+n+c

print(func2(6,7))
