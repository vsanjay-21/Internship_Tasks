# 20. Super Reduced String
# https://www.hackerrank.com/challenges/reduced-string/submissions/code/485569154
def string(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
            
    if not stack:
        return "Empty String"
    else:
        return "".join(stack)

if __name__ == '__main__':
    s = input()
    print(string(s))
