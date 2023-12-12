def judgeCircle(moves):
    x, y = 0, 0

    for m in moves:
        if m == 'U':
            y += 1
        elif m == 'D':
            y -= 1
        elif m == 'R':
            x += 1
        else:
            x -= 1
    
    return (x,y) == (0,0)
    

# Testcases:
# Testcase 1
moves = 'LL'
print('Testcase 1: Moves = {0}'.format(moves))    
print(judgeCircle(moves))

# Testcase 2
moves = 'UD'
print('Testcase 2: moves = {0}'.format(moves))    
print(judgeCircle(moves))
