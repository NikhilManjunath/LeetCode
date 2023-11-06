def backspaceCompare(s: str, t: str) -> bool:
    i, j = len(s)-1, len(t)-1
    skip_i, skip_j = 0,0

    while i >= 0 and j >= 0:
        s_char, t_char = '', ''

        while s_char == '' and i >= 0:
            if s[i] == '#':
                skip_i += 1
            elif skip_i > 0:
                skip_i -= 1
            else:
                s_char = s[i]
            i = i - 1

        while t_char == '' and j >= 0:
            if t[j] == '#':
                skip_j += 1
            elif skip_j > 0:
                skip_j -= 1
            else:
                t_char = t[j]
            j = j - 1

        if s_char != t_char:
            return False

    return True

# Testcases:
s,t = "ab#c", "ad#c"
print('Testcase 1: s = {0}, t = {1}'.format(s,t))    
print(backspaceCompare(s,t))
