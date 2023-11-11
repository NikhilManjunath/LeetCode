def countSubstrings(s: str) -> int:
    count = 0
    for i in range(len(s)):
        l,r = i,i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        
        l,r = i,i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1

    return count
    

# Testcases:
# Testcase 1
s = 'abc'
print('Testcase 1: s = {0}'.format(s))    
print(countSubstrings(s))

# Testcase 2
s = 'aaa'
print('Testcase 2: s = {0}'.format(s))    
print(countSubstrings(s))
