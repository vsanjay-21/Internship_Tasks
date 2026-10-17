# 8. Set .add()
# https://www.hackerrank.com/challenges/py-set-add/submissions/code/485386387
if __name__ == "__main__":
    n = int(input())
    
    a = set()
    
    for i in range(n):
        a.add(input().strip())
        
    print(len(a))
