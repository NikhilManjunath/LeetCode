First Unique Character in a String - Leetcode Easy

Question: 
Given a string 's', return the index of the first non-repeating Character. If it does not exist, return -1

Solution:
Create a dictionary for storing the count of each letter in the string. Go through each letter and fill the dictionary

Once again, iterate through the string to identify the first character that occurred only once in the string

Time Complexity:
O(n+n) = O(2n) = O(n)

Space Complexity:
O(26) = O(1)
        
