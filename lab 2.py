a = float(input("a-ni daxil et: "))

b = 6.0
while b <= 10.0:
    if b - 2 * a < 2:
        y = 2 * a**2 + b
    elif b - 2 * a == 2:
        y = 3 * b - a
    else:
        y = 9 * a + b**2

    print(f"b = {b:.1f} → y = {y}")
    b += 0.5
