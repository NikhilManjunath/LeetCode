def fractionToDecimal(numerator: int, denominator: int) -> str:
    if numerator == 0:
        return "0"
    
    res = []

    if (numerator < 0 <= denominator) or (denominator < 0 <= numerator):
        res.append('-')
    
    numerator = abs(numerator)
    denominator = abs(denominator)

    res.append(str(numerator//denominator))

    r = numerator % denominator
    
    if r == 0:
        return ''.join(res)
    
    res.append('.')
    
    remainder_map = {}
    while r != 0:
        if r in remainder_map:
            res.insert(remainder_map[r],'(')
            res.append(')')
            break

        remainder_map[r] = len(res)
        r *= 10
        res.append(str(r // denominator))
        r %= denominator
    
    return ''.join(res)
    

# Testcases:
# Testcase 1
num, den = 1, 2
print('Testcase 1: numerator = {0} and denominator = {1}'.format(num, den))    
print(fractionToDecimal(num, den))

# Testcase 2
num, den = 4, 333
print('Testcase 1: numerator = {0} and denominator = {1}'.format(num, den))    
print(fractionToDecimal(num,den))
