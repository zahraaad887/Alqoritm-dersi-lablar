n = int(input())
ededler = []

for i in range(n):
    eded = int(input())
    ededler.append(eded)

with open("massiv.txt", "w") as f:
    for eded in ededler:
        f.write(str(eded) + "\n")

cut_ededler = []
cut_cem = 0

with open("massiv.txt", "r") as f:
    for line in f:
        eded = int(line.strip())
        if eded % 2 == 0:
            cut_ededler.append(eded)
            cut_cem += eded

with open("cut_ededler.txt", "w") as f2:
    for eded in cut_ededler:
        f2.write(str(eded) + "\n")

print( cut_cem)
