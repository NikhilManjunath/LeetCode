Reaching Points - LeetCode Hard

Given (sx,sy) we need to see if can reach (tx,ty) by only doing:
    either (sx,sy+sx) 
    or (sx+sy,sy)

Also: sx,sy,tx,ty are all greater than 0

Every parent (x,y) has 2 children (x,x+y) and (x+y,y).
However, every point (x,y) can have only 1 parent:
    (x-y,y) if x >= y
    (x,y-x) if y > x
(Because we cannot have x,y < 0)

Hence we go through a while loop trying to come from tx,ty to sx,sy

