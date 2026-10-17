# 19. Merge the Tools!
# https://www.hackerrank.com/challenges/merge-the-tools/submissions/code/485452035
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        c = string[i : i + k]
        b = "".join(dict.fromkeys(c))
        print(b)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
