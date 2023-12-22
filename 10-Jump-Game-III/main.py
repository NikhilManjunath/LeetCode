def canReach(arr, start):
    # BFS
    # q = [start]

    # while q:
    #     node = q.pop(0)
    #     if arr[node] == 0:
    #         return True
        
    #     if arr[node] < 0:
    #         continue

    #     for i in [node + arr[node], node - arr[node]]:
    #         if 0 <= i < len(arr):
    #             q.append(i)
        
    #     arr[node] = -arr[node]
    # return False
    
    # DFS
    if 0 <= start < len(arr) and arr[start] >= 0:
        if arr[start] == 0:
            return True
        
        arr[start] = -arr[start]

        return canReach(arr,start-arr[start]) or canReach(arr,start+arr[start])
    return False

# Testcases:
# Testcase 1
arr = [4,2,3,0,3,1,2]
start = 5
print('Testcase 1: Array = {0}, Start = {1}'.format(arr,start))    
print(canReach(arr,start))

# Testcase 2
arr = [4,2,3,0,3,1,2]
start = 0
print('Testcase 2: Array = {0}, Start = {1}'.format(arr,start))    
print(canReach(arr,start))

# Testcase 3
arr = [3,0,2,1,2]
start = 2
print('Testcase 3: Array = {0}, Start = {1}'.format(arr,start))    
print(canReach(arr,start))