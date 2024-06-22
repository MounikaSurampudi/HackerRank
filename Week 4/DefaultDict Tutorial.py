from collections import defaultdict
n, m = map(int, input().split())
A = list(input() for _ in range(n))
B = list(input() for _ in range(m))
d = defaultdict(list)
for i in range(m):
    if B[i] in A:
        for j in range(n):
            if B[i] == A[j]:
                d[i].append(j+1)
    else:
        d[i].append(-1)
for i in d.values():
    print(' '.join(str(_) for _ in i))
