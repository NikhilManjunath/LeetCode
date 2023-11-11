Robot Bounded In Circle: Leetcode Medium

Question:
Given a robot initially starting at (0,0) in an infinite plane and facing north, find out if it will travel in a circle if a given set of instructions is repeated forever.

Solution:
For the robot to travel to travel in a circle -> it must return to (0,0).

It can return to (0,0) only in 2 conditions:
    i.  One run of the instruction set results in robot back at (0,0)
    ii. At the end of 1 run, the robot is facing a different direction.

Check for these 2 possibilities and if either is True, then the robot is travelling in a circle

Time Complexity:
O(N)
We iterate through the instructions set only once

Space Complexity:
O(1)