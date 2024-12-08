'''
Problem statement
Ninja was given an integer ‘N’. For each number from ‘0’ to ‘N’, he must print the number of set bits present in its binary representation.

For example:

The binary representation of ‘5’ is 101. Therefore the number of set bits is 2.
Detailed explanation ( Input/output format, Notes, Images )
Constraints -
1 <= ‘T’ <= 10
0 <= ‘N’ <= 10^5 
Note- Sum of ‘N’ over all test cases does not exceed 10^5.

Time Limit: 1 sec
Sample Input-1
2
3
5
Sample Output-1
0 1 1 2
0 1 1 2 1 2
Explanation for Sample Input 1:
For test case 1:
    The binary representation of 0 is ‘0’. Hence the total set bit is 0.
    The binary representation of 1 is ‘1’. Hence the total set bit is 1.
    The binary representation of 2 is ‘10’. Hence the total set bit is 1.
    The binary representation of 3 is ‘11’. Hence the total set bit is 2.
Sample Input -2
 2
 0
 2
Sample Output -2
0
0 1 1
'''

from collections import *
from math import *

from typing import *

def count(N: int) -> List[int] :
    a=[0] 
    for i in range(1,N+1):
        c=str(bin(i).count('1'))
        a.append(c)
    return a