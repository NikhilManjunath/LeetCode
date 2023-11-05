def isRobotBounded(instructions):
        # N = (0,1)
        # S = (0,-1)
        # E = (1,0)
        # W = (-1,0)

        x,y = 0,0
        dx,dy = 0,1
        for ins in instructions:
            if ins == 'G':
                x, y = x+dx, y+dy
            elif ins == 'L':
                dx,dy = -dy,dx
            else:
                dx,dy = dy,-dx
        
        return (x,y) == (0,0) or (dx,dy) != (0,1)


# Testing
print('Program to find out if a robot exists in a circle')

inst_1 = 'GL'
print('Testcase 1: Instruction: {0}'.format(inst_1))
print(isRobotBounded(inst_1))

inst_2 = 'GGLLGG'
print('Testcase 2: Instruction: {0}'.format(inst_2))
print(isRobotBounded(inst_2))

inst_3 = 'GG'
print('Testcase 3: Instruction: {0}'.format(inst_3))
print(isRobotBounded(inst_3))