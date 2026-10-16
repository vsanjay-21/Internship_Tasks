if __name__ == "__main__":
    a, b = map (int, input().split())
    
    arr = list(map(int, input().split()))
    
    c = set(map(int, input().split()))
    d = set(map(int, input().split()))
    s = 0
    
    for i in arr:
        if i in c:
            s += 1
        elif i in d:
            s -= 1
            
    print(s)
