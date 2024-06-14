A = set(map(int, input().split()))

for i in range(int(input())):
    B = set(map(int, input().split()))
    if not A.issuperset(B) or len(A) == len(B):
        print(False)
        exit()
        
print(True)
