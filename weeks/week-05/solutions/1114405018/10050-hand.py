import sys

def main() -> None:
    nums = list(map(int, sys.stdin.read().split()))
    if not nums:
        return

    t = nums[0]  
    i = 1
    ans = []

    for _ in range(t):
        n = nums[i] 
        i += 1
        p = nums[i] 
        i += 1

        hartals = nums[i:i + p] 
        i += p
    
        lost = set() 

        for h in hartals:
            day = h
            while day <= n:
                if day % 7 != 6 and day % 7 != 0:
                    lost.add(day)
                day += h

        ans.append(str(len(lost)))
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()
