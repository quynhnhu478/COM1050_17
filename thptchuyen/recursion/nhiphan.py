def nhiphan(n):
    if n>1: nhiphan(n//2)
    print(n%2,end='')
n=int(input())
a=[int(input()) for i in range(n)]
for i in range(n):
   nhiphan(a[i])
   print(end='\n')
