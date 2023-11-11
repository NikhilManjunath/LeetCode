def firstUniqChar(s: str) -> int:
    hashmap = {}
    for i in s:
        hashmap[i] = hashmap.get(i,0) + 1
    
    for i in range(len(s)):
        if hashmap[s[i]] == 1:
            return i
    
    return -1

# Testcases:
# Testcase 1
s = 'leetcode'
print('Testcase 1: s = {0}'.format(s))    
print(firstUniqChar(s))

# Testcase 2
s = 'loveleetcode'
print('Testcase 2: s = {0}'.format(s))    
print(firstUniqChar(s))

# Testcase 3
s = 'aabb'
print('Testcase 3: s = {0}'.format(s))    
print(firstUniqChar(s))
