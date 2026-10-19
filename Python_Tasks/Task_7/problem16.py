# 16. Caesar Cipher
# https://www.hackerrank.com/challenges/caesar-cipher-1/submissions/code/485568549
def caesar(s, k):
    result = []
    for char in s:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + k) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    return "".join(result)

if __name__ == '__main__':
    n = int(input())
    s = input()
    k = int(input())
    print(caesar(s, k))
