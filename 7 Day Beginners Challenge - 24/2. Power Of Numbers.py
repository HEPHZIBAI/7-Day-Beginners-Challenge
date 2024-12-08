'''
Problem statement
You are given a number 'N' and its reverse 'R'.



Return the number raised to the power of its own reverse. As answers can be very large, print the result modulo '10^9 + 7'.



For Example:

For 'N' = 20, 'R' = 2
The answer is 400 since 20^2 as the reverse of 20 is 2.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
14 41
Sample Output 1:
722400406 
Explanation of sample output 1:
'N' = 14
Answer is 14^41 as the reverse of 14 is 41.
when divided by 1000000007 gives remainder as 722400406
Sample Input 2:
2 2
Sample Output 2:
4
Constraints:
1 <= N <= 10^9
Time Limit: 1 sec
'''

from typing import *

def power(N : int, R : int) -> int:
    MOD = 10**9 + 7
    return pow(N, R, MOD)