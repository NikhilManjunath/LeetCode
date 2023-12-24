Find the Winner of the Circular Game - Leetcode Medium

Question: 
There are 'n' friends playing a game. They are sitting in a circle and numbered from 1 to n in CLOCKWISE ORDER.
Rules of the game:
1. Start at 1st friend
2. Count k friends in the clockwise direction (including the friend you started at)
3. Last friend you counted loses and leaves the game
4. Start again with the friend next to the eliminated friend and continue until there is a single winner

Ex:
1. n = 5, k = 2
   output: 3
   [1,2,3,4,5] -> start at 1. 2 eliminated
   [1,3,4,5]   -> start at 3. 4 eliminated
   [1,3,5]     -> start at 5. 1 eliminated
   [3,5]       -> start at 3. 5 eliminated
   3 is the winner


Solution:
1. Make a list of n numbers starting from 1 to n
2. First find out which index friend needs to be eliminated
3. Eliminate the friend. Update the index
4. Repeat until the list contains only a single element
        
Time Complexity: O(N)
# Going through the list at max n times

Space Complexity: O(N)
# n variables in list created