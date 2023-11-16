S = float
n = 2
i = 0
S = 3
while i <= 15:
    if i % 2 == 0:
        S = S + (4 / (n * (n + 1) * (n + 2)))
    n = n+2
    i = i+1
    print(S)
    if i % 2 == 1:
        S = S - (4 / (n * (n + 1) * (n + 2)))
    n = n + 2
    i = i + 1
    print(S)