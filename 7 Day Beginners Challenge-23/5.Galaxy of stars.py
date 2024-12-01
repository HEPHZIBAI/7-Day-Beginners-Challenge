'''
Problem statement
Ninja wants to build a star pattern for a given odd number.

The pattern for ‘N’ = 7  will look like this:

*
**
***
****
***
**
*
Your task is that for a given odd integer 'N', print the pattern.

Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 5
1 <= N <= 99

Time Limit: 1 sec
Sample Input 1:
2
3
5
Sample Output 1:
*
**
*
*
**
***
**
*
Explanation of Sample Input 1:
Test case 1:

In the first test case of sample input 1, we need to print a triangle-like pattern wherein each line, the number of stars will be increasing till the central row and then it starts decreasing. So for n=3, till 2nd-row stars increase and then start decreasing.
Sample Input 2:
1
1
Sample Output 2:
*
Explanation of Sample Input 2:
Test case 1:
As ‘N’ is equal to ‘1’, we just need to print one line. 
'''

def galaxyofStar(n):
	a=[]
	for i in range(1,(n//2)+2):
		print("*" * i)
	for i in range(n//2,0,-1):
		print("*" * i)
	return a