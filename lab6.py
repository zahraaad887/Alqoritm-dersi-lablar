n = int(input())
m = int(input())


A = []
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

sum = 0
for i in range(n):
    for j in range(m):
        sum += A[i][j]

print(sum)
