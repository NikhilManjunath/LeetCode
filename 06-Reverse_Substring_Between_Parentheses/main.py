def reverseParentheses(s: str) -> str:
    stack = []
    for i in range(len(s)): 
        if s[i] != ')':
            stack.append(s[i])
        
        else:
            rev = []
            while stack[-1] != '(' and len(stack) > 0:
                rev.append(stack.pop())
            stack.pop()
            for i in rev:
                stack.append(i)
        
    return ''.join(stack)
    

# Testcases:
# Testcase 1
s = '(abcd)'
print('Testcase 1: s = {0}'.format(s))    
print(reverseParentheses(s))

# Testcase 2
s = '(u(love)i)'
print('Testcase 2: s = {0}'.format(s))    
print(reverseParentheses(s))

# Testcase 3
s = '(ed(et(oc))el)'
print('Testcase 3: s = {0}'.format(s))    
print(reverseParentheses(s))
