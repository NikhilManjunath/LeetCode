Jump Game III - Leetcode Medium

Question: 
Given an array of non-negative integers arr, you are initially positioned at start index of the array. 
When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.
Notice that you can not jump outside of the array at any time.

Ex:
1. arr = [4,2,3,0,3,1,2], start = 5
   output: True 
   # 2 ways possible: 5 -> 4 -> 1 -> 3 OR 5 -> 6 -> 4 -> 1 -> 3


Solution:
Either DFS or BFS can be done

BFS:
1. Initialize a queue and add the start to it
2. Go through each node in the queue FIFO:
3. If arr[node] == 0, then we have reached the index with value 0
4. If not, set the value of the node to its negative (arr[node] = -arr[node]) so that we dont visit the same node again
5. Now check for node + arr[node] and node - arr[node] IFF these two indices are within the array (0 <= i < len(arr))
6. Return False if not possible

DFS:
1. Check if start index lies within the array (0 <= start < len(arr)). Als check if arr[start] >= 0 so that we dont visit the nodes already visited
2. Check if arr[start] == 0. If yes, return True
3. If not, set value of this node to its negative (arr[start] = -arr[start]) so that we do not visit again
4. Repeat for start + arr[start] and start - arr[start]
5. Return False if not possible
        
