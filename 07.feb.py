import time

def _sum():
    s = 0
    for i in range(1000000):
        s += i
    return s


start = time.time()
print(_sum())
end = time.time()
print("time taken: ", end -start)





# Decorator definition
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)   # run the original function
        end = time.time()
        print(f"Time taken by {func.__name__}: {end - start:.6f} seconds")
        return result
    return wrapper

# Apply decorator
@timing_decorator
def _sum():
    s = 0
    for i in range(1000000):
        s += i
    return s

# Run function
print(_sum())

 


def reversing(l):
    i = 0
    j = len(l) - 1
    while i < j:
        l[i], l[j] = l[j], l[i]
        i += 1
        j -= 1
    return l


l= [i for i in range(10)]
reversing(l)
print(l)

l = ["python", 1,2,"genai",5]
reversing(l)
print(l)


def reversing_recursive(l, i=0, j=None):
    if j is None:
        j = len(l) - 1
    
    # Base case: stop when indices meet or cross
    if i >= j:
        return l
    
    # Swap elements
    l[i], l[j] = l[j], l[i]
    
    # Recursive call on inner sublist
    return reversing_recursive(l, i+1, j-1)


# Example
print(reversing_recursive([1, 2, 3, 4, 5]))





def decfun(func):
    def wrapper(n):
        print(f"fibnocci enter with ({n})")
        res = func(n)
        print(f"fibnocci exit with ({n})")
        return res
    return wrapper

@decfun
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(3))





# Day 1 of my Python Practice 🚀  
# Today I focused on the basics of constructing a program in Python. Here are five small exercises I worked on:

# 1. Add and Subtract
a, b = 10, 5
print(a, "+", b, "=", a+b)
print(a, "-", b, "=", a-b)

# Output:
# 10 + 5 = 15
# 10 - 5 = 5


# 2. Multiply and Divide
x, y = 8, 4
print(x, "*", y, "=", x*y)
print(x, "/", y, "=", x/y)

# Output:
# 8 * 4 = 32
# 8 / 4 = 2.0

# 3. Square and Cube
n = 4
print(n, "² =", n**2)
print(n, "³ =", n**3)

# Output:
# 4 ² = 16
# 4 ³ = 64

# 4. Square Root
import math
m = 25
print("√", m, "=", math.sqrt(m))

# Output:
# √ 25 = 5.0

# 5. Area and Perimeter of a Square
side = 6
print("Area =", side**2)
print("Perimeter =", 4*side)

# Output:
# Area = 36
# Perimeter = 24
