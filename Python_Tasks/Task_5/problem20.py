# 20. Piling Up!
# https://www.hackerrank.com/challenges/piling-up/submissions/code/485453811
if __name__ == "__main__":
    a = int(input())
    
    for _ in range(a):
        n = int(input())
        b = list(map(int, input().split()))
        
        l = 0
        r = n - 1
        c = float("inf")
        p = True
        
        while l <= r:
            if b[l] >= b[r]:
                current = b[l]
                l += 1
            else:
                current = b[r]
                r -= 1
                
            if current > c:
                p = False
                break
                
            c = current
        if p:
            print("Yes")
        else:
            print("No")
