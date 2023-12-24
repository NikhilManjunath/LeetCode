Asteroid Collision - Leetcode Medium

Question: 
Given an array of asteroids, represented by their size and direction, return the asteroids remaining after Collision

Ex:
1. arr = [10,2,-5]
   output: [10] 
   # 10 and 2 going in the same direction so no collision. 
   -5 going towards 2. Since abs(-5) > abs(2), 2 is destroyed as it is smaller.
   -5 now goes towards 10 but is smaller and hence -5 is destroyed. 
   Hence only 10 remains

Solution:
Collision only happens if:
The current asteroid is going in the negative direction AND the previous asteroid is going in the positive direction
(If current asteroid is going in the positive and previous is going in the negative, then they will not collide)

Hence:
1. Iterate through the asteroids list
2. If asteroid moving in positive direction, add it to result queue
2. If current asteroid is moving in negative direction, perform collisions until the current asteroid is destroyed or the previous asteroid is moving in the same direction or there are no previous asteroids left
3. If negative asteroid is not destroyed after check, add it to the result queue
        
Time Complexity: O(N)
Space Complexity: O(N)