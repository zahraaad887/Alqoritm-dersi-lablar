import math

def f(x):
    return math.sqrt(x) * math.cos(math.sqrt(x))

def iteration_method(x0, tol=1e-5, max_iter=1000):
    x = x0
    for i in range(max_iter):
        x_new = x - f(x)  # Sadə iterasiya addımı (bu, tam dəqiq olmaya bilər)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    print("Maximum iteration reached without convergence.")
    return x

root = iteration_method(0.5)
print("Root:", root)
