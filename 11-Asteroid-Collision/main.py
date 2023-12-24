def asteroidCollision(asteroids):
    res = []

    for a in asteroids:
        while res and a < 0 and res[-1] > 0:
            if a + res[-1] < 0:
                res.pop()
            elif a + res[-1] == 0:
                res.pop()
                a = 0
            else:
                a = 0
        
        if a:
            res.append(a)
    
    return res

# Testcases:
# Testcase 1
asteroids = [5,10,-5]
print('Testcase 1: asteroids = {0}'.format(asteroids))    
print(asteroidCollision(asteroids))

# Testcase 2
asteroids = [-8,8]
print('Testcase 2: asteroidsay = {0}'.format(asteroids))    
print(asteroidCollision(asteroids))

# Testcase 3
asteroids = [10,2,-5]
print('Testcase 3: asteroidsay = {0}'.format(asteroids))    
print(asteroidCollision(asteroids))