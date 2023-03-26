# Задание 10
n = int(input())
countZero = 0
countOne = 0
for i in range(n):
    x = int(input())
    if x == 0:
        countZero += 1
    else:
        countOne += 1
if countOne > countZero:
    print(countZero)
else:
    print(countOne)



# Задание 12
S = int(input())
P = int(input())
c = False 
for i in range(S + P):
    if c:
        break
    for j in range(S + P):
        if i + j == S and i * j == P:
            c = True
            print(*sorted([i, j]))
            break


# Задание 14
n = int(input())
i = 0
while 2 ** i <= n:
    print(2 ** i)
    i += 1
