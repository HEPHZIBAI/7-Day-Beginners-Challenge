'''
def kthRow(k):
    row = [1]
    for i in range(1, k):
        # Create the next row using the previous row
        row.append(1)  # add the last element
        for j in range(i-1, 0, -1):
            row[j] += row[j-1]  # Update the elements in place
    return row

'''

Problem statement
You are given a non-negative integer 'K'. Your task is to find out the Kth row of Pascal’s Triangle.

In Mathematics, Pascal's triangle is a triangular array where each entry of a line is a value of a binomial coefficient. An example of Pascal’s triangle is given below.


Example :-

INPUT : K = 2
OUTPUT: 1 1

In the above example, K = 2, Hence the 2nd row from the top of pascal’s triangle, as shown in the above example is 1 1.

INPUT   : K = 4
OUTPUT  : 1 4 6 4 1

In the above example, K = 4, Hence the 4th row from the top of pascal’s triangle, as shown in the above example is 1 3 3 1.
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 50
1 <= K <= 50

Where ‘T’ is the number of test cases, ‘K’ is the input row number.

Time limit: 1 sec.
Sample Input 1:
4
1
2
3
4
Sample Output 1:
1
1 1
1 2 1
1 3 3 1
Explanation of sample input 1:
For K = 1, the elements of the first row of the pascal’s triangle will be printed, Hence the output is 1.

For K = 2, the elements of the second row of the pascal’s triangle will be printed, Hence the output is 1 1.

For K = 3, the elements of the third row of the pascal’s triangle will be printed, Hence the output is 1 2 1.

For K = 4, the elements of the fourth row of the pascal’s triangle will be printed, Hence the output is 1 3 3 1.
Sample Input 2:
5
6
5 
7
2
9
Sample Output 2:
1 5 10 10 5 1 
1 4 6 4 1 
1 6 15 20 15 6 1 
1 1
1 8 28 56 70 56 28 8 1 