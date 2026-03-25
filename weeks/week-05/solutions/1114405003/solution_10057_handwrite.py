def solve(n):
    n.sort()
    l=n[len(n)//2-1] if len(n)%2==0 else n[len(n)//2]
    u=n[len(n)//2] if len(n)%2==0 else l
    d=[abs(x-l) for x in n]
    return l,sum(1 for x in d if x==min(d)),u-l+1

print(solve([5]))
print(solve([1,3,5]))
print(solve([1,5]))
print(solve([5,5,5]))
