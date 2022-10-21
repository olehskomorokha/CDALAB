N = 0
while N <= 100:
    N = int(input('input N > 100: '))
i = 10
S = 10
while i < N:
    i += 1
    S = S + pow(i, 2)
    print(S)