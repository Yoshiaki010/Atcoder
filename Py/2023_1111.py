"""
#lv1
n,x=map(int,input().split())
s=list(map(int,input().split()))
ans=0
for i in range(n):
    if s[i] <= x:
        ans+=s[i]
print(ans)
"""
#lv2
"""
n=int(input())
d=list(map(int,input().split()))
ans=0
for i in range(n):
    m=str(i+1)
    setm=set(list(m))
    if len(setm) == 1:
        date=int(m[-1])
        if (date*10+date) <= d[i]:
            ans+=2
        elif date <= d[i]:
            ans+=1
print(ans)
"""
#lv3
"""
n,q=map(int,input().split())
s=list(input())
for _ in range(q):
    ans=0
    l,r=map(int,input().split())
    now = s[l-1:r]
    left=now[0::2]
    right=now[1::2]
    if n%2 == 0:
        left+=["X"]
    for i in range(len(right)):
        if left[i] == right[i]:
            ans+=1
        if left[i+1] == right[i]:
            ans+=1
    print(ans)
"""
n,q=map(int,input().split())
s=list(input())
anss=[]
left=s[0::2]
right=s[1::2]
if n%2 == 0:
    left+=["X"]
for i in range(len(right)):
    if left[i] == right[i]:
        anss.append(1)
    else:
        anss.append(0)
    if left[i+1] == right[i]:
        anss.append(1)
    else:
        anss.append(0)
print(anss)
for _ in range(q):
    ans=0
    l,r=map(int,input().split())
    now = anss[l-1:r-1]
    ans= sum(now)
    print(ans)
