Reverse Substrings Between Each Pair of Parentheses - Leetcode Medium

Question: 
Given a string 's' consisting of lower case letters and brackets, reverse the strings in each pair of matching parentheses, starting from innermost one.
Result should not contain any brackets

Ex: (ed(et(oc))el) -> (ed(etco)el) -> (edocteel) -> leetcode

Solution:
1. Initialize a stack to add our characters.
2. Iterate through the string:
    If char != ')':
        add the char to the stack
    Else:
        pop the stack to a list until we have removed the latest '(' and then add the elements back to the stack without '('

3. Return the stack as a list


Time Complexity:
O(N)    (because we iterate through the string only once)

Space Complexity:
O(N)
        
