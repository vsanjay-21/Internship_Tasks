# 17. Separate the Numbers
# https://www.hackerrank.com/challenges/separate-the-numbers/submissions/code/485568692
def separate(s):
    for i in range(1, len(s) // 2 + 1):
        first = s[:i]
        if first[0] == '0':
            break
            
        num = int(first)
        temp = first
    
        while len(temp) < len(s):
            num += 1
            temp += str(num)
            
        if temp == s:
            print(f"YES {first}")
            return
            
    print("NO")

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        s = input()
        separate(s)
