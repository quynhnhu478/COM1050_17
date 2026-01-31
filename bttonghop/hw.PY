s=input()
d1,d2,d3,d4,d5,d6=0,0,0,0,0,0
for i in s:
    if i=='(': d1+=1
    if i==')': d2+=1
    if i=='[': d3+=1
    if i==']': d4+=1
    if i=='{': d5+=1
    if i=='}': d6+=1
if d1==d2 and d3==d4 and d5==d6:
    print("Yes")
else:
    print("No")

