def reachingPoints(sx: int, sy: int, tx: int, ty: int) -> bool:
    if sx == tx and sy == ty:
        return True
    
    while tx >= sx and ty >= sy:
        if ty > tx:
            if tx > sx:
                ty %= tx
            else:
                return (ty-sy)%tx == 0
        
        else:
            if ty > sy:
                tx %= ty
            else:
                return (tx-sx)%ty == 0
    
    return tx == sx and ty == sy


# Testing
sx, sy, tx, ty = 1, 1, 2, 2
print('Testcase 1: sx = {0}, sy = {1}, tx = {2}, ty = {3}'.format(sx,sy,tx,ty))
print(reachingPoints(sx,sy,tx,ty))

sx, sy, tx, ty = 1, 1, 3, 5
print('Testcase 2: sx = {0}, sy = {1}, tx = {2}, ty = {3}'.format(sx,sy,tx,ty))
print(reachingPoints(sx,sy,tx,ty))

sx, sy, tx, ty = 1, 1, 1, 1
print('Testcase 3: sx = {0}, sy = {1}, tx = {2}, ty = {3}'.format(sx,sy,tx,ty))
print(reachingPoints(sx,sy,tx,ty))