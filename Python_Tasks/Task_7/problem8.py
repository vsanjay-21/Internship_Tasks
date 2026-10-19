# 8. Gemstones
# https://www.hackerrank.com/challenges/gem-stones/submissions/code/485567752
def gemstones(arr):
    common = set(arr[0])
    for rock in arr[1:]:
        common.intersection_update(set(rock))
    return len(common)

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(input())
    print(gemstones(arr))
