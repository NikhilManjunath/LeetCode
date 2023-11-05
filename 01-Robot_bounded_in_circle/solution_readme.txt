Robot Bounded In Circle: Leetcode Medium

In this question, we need to find out if a robot initially starting at (0,0) in an infinite plane and facing north will travel in a circle if a given set of instructions is repeated forever.

For the robot to travel to travel in a circle -> it must return to (0,0).

It can return to (0,0) only in 2 conditions:
    i.  One run of the instruction set results in robot back at (0,0)
    ii. At the end of 1 run, the robot is facing a different direction.

Check for these 2 possibilities and if either is True, then the robot is travelling in a circle