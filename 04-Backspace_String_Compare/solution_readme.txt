Backspace String Compare - Leetcode Medium

Question: Given 2 strings: s and t, return true if they are equal when typed into text editors.
'#' means a backspace character

Solution:
- We can compare each valid element of the strings in each step. Whenever the elements do not match up, we return False. Else, if all match, we return true

- It is better to iterate from the end as we need to incorporate backspace ('#'). This way, if the element is '#', we can skip the element that comes before '#' in the string.
    - hence we initialize i, j to the lenghts of the 2 strings

- We also need to track the number of backspaces:
    - hence use skip_i, skip_j to track how many elements to skip/delete

- While loop:
    - each time get the valid element for s,t -> Compare -> return False if no match

    - the while loop itself has 3 different outcomes for each string:
        - '#' element which means we increase the skip value by 1
        - skip > 0: which means we skip 1 element and decrease the skip value by 1
        - neither of the above two: in which case, we have our valid element
        
