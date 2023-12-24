def findTheWinner(n,k):
    num_list = [i for i in range(1,n+1)]

    index = 0
    while len(num_list) > 1:
        index = (index + k - 1) % len(num_list)
        num_list.pop(index)

    return num_list[0]


# Testcases:
# Testcase 1
n = 5
k = 2
print('Testcase 1: n = {0}, k = {1}'.format(n,k))    
print(findTheWinner(n,k))

# Testcase 2
n = 5
k = 4
print('Testcase 2: n = {0}, k = {1}'.format(n,k))    
print(findTheWinner(n,k))

# Testcase 3
n = 6
k = 5
print('Testcase 3: n = {0}, k = {1}'.format(n,k))    
print(findTheWinner(n,k))