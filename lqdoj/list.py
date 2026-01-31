n=int(input())
a=list(map(int,input().strip().split()))
ans=0
for i in range(n):
    dem={}
    loai_so=0
    dem_3=0
    for j in range(i,n):
        if a[j] in dem:
            dem[a[j]]+=1
        else:
            dem[a[j]]=1
            loai_so+=1
        if dem[a[j]]==3:
            dem_3+=1
        elif dem[a[j]]==4:
            break
        if loai_so==dem_3:
            ans+=1
print(ans)
        