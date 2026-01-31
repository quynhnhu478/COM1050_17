n = int(input())
a = list(map(int, input().strip().split()))
vt, vt1 = -1, -1
for i in range(n):
    if a[i] > 0:
        vt = i + 1 
        break
for i in range(n - 1, -1, -1):
    if a[i] > 0:
        vt1 = i + 1     
        break
print(vt, vt1)