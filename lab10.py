import math
def f(x):
    return math.log(x) - math.sqrt(x)
def f_prime(x):
    return 1/x - 1/(2 * math.sqrt(x))
def newton_method(x0, tol=1e-5, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        fpx = f_prime(x)
        if fpx == 0:
            raise ValueError("The derivative is equal to 0. Newton's method is stopped..")
        x_new = x - fx / fpx
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x
root = newton_method(0.5)
print("Root:", root)
