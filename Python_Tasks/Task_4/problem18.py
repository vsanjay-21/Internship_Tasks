if __name__ == '__main__':
    N = int(input())
    m = []
    
    for i in range(N):
        a = input().split()
        b = a[0]
        c = list(map(int, a[1:]))
        
        if b == "print":
            print(m)
        else:
            getattr(m, b)(*c)
