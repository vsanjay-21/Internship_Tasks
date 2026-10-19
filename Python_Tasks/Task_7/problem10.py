# 10. CamelCase
# https://www.hackerrank.com/challenges/camelcase/submissions/code/485567942
def camel(s):
    count = 1
    for i in s:
        if i.isupper():
            count += 1
    return count

if __name__ == '__main__':
    s = input()
    print(camel(s))
