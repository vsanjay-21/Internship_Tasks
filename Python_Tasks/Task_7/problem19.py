# 19. Weighted Uniform Strings
# https://www.hackerrank.com/challenges/weighted-uniform-string/submissions/code/485569031
def weighted(s, queries):
    weights = set()
    prev_char = ""
    current_weight = 0
    
    for i in s:
        weight = ord(i) - ord('a') + 1
        if i == prev_char:
            current_weight += weight
        else:
            current_weight = weight
            prev_char = i
        weights.add(current_weight)
        
    result = []
    for q in queries:
        if q in weights:
            result.append("Yes")
        else:
            result.append("No")
    return result

if __name__ == '__main__':
    s = input()
    count = int(input())
    queries = []
    for _ in range(count):
        queries.append(int(input()))
        
    result = weighted(s, queries)
    print('\n'.join(result))
