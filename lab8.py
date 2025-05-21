import math

def f(x):
    return math.sqrt(x) * math.cos(math.sqrt(x))

def bisection(a, b, tol=1e-5):
    if f(a) * f(b) >= 0:
        print("Bisection method is not suitable (f(a) and f(b) have the same sign).")
        return None
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

root = bisection(0.4, 0.6)
print("Root:", root)
