Fraction to Recurring Decimal - Leetcode Medium

Question: 
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If fractional part is repeating, enclose the repeating part in parentheses.

Ex:
1. num = 1, den = 2
   output: "0.5"

2. num = 4, den = 333
   output: "0.(012)"

Solution:
1. Check if num = 0:
    If yes, return 0

2. Initialize a list. Check if either num or den is negative:
    If yes, add "-" to list

3. Divide num by den and add the quotient (//) to the list

4. If remainder is 0, return list as a string

5. Else:
    - Add a '.' to the list
    - Create a hashmap to track the position for repeating sequence. The key will be remainder and the value will be the position of remainder value in the list
    - If remainder already in hashmap keys:
        add '(' to the list at the position where the repeating char was found. Then add ')' at the end.
        return the list as a string
    - store the remainder as key in the hashmap, multiply by 10 and add it to list (remainder // denominator), calculate the new remainder

6. return list as a string


        
