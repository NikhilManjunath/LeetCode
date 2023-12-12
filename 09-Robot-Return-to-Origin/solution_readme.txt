Robot Return to Origin - Leetcode Easy

Question: 
Given a robot starting at origin on a 2D plane and a sequence of its moves, judge if the robot ends back at the origin after it completes its moves

Ex:
1. moves = 'LL'
   output: False 
   # it ends up at (-2,0)

2. moves = 'UD
   True

Solution:
1. Initialize x,y to 0,0
2. For each move in the sequence, change the value of x or y by 1 in the direction of movement
    x = x + 1 if Right else x - 1
    y = y + 1 if Up else y - 1
3. Check if the latest position of robot is (0,0)

Alternate Solution:
1. Count the number of 'L','R','U','D' in the sequence
2. If count(L) == count(R) AND count(U) == count(D):
    return True

        
