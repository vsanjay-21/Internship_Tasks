# 9. Word Order
# https://www.hackerrank.com/challenges/word-order/submissions/code/485386612
if __name__ == "__main__":
    n = int(input())
    
    count = {}
    
    for i in range(n):
        a = input().strip()
        count[a] = count.get(a, 0) + 1
        
    print(len(count))
    print(*count.values())
