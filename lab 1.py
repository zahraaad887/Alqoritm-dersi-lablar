import math

m-nin hesablanması
numerator = (1234*2)*(1/3) * math.log(2)
denominator = 1.124 * math.sqrt(0.024) * math.cos(1)
m = numerator / denominator

r-nin hesablanması
r = math.sin(-0.25 * (math.atan(2) + math.atan(3)))

s-nin hesablanması
if r > -2 * m:
    s = math.exp(-abs(m / r))
else:
    s = m * r

Nəticələri çap edək
print(f"m = {m}")
print(f"r = {r}")
print(f"s = {s}")
