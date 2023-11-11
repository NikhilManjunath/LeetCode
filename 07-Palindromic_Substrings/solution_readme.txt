Palindromic Substrings - Leetcode Medium

Question: 
Given a string 's' return the number of palindromic substrings in it.

Ex: 'aaa' => 6 (a,a,a,aa,aa,aaa)

Solution:
1. Iterate through the string:
    1.1 finding substrings whose length is odd (1,3,5..)
        Initialize l = i, r = i
        while s[i] == s[j] and l > 0 and r < len(s):
            increase count(palindrome) by one, l -= 1, r += 1
    
    1.2 finding substrings whose length is odd (2,4,6..)
        Initialize l = i, r = i+1
        Do the same if condition as 1.1



Time Complexity:
O(N^2)
because in the worst case scenario our while loops iterate over each character in the string

Space Complexity:
O(1)
        
