#! python3

"""
Count by 2's and display all the numbers, 1 on each line.
Continue until the current value is 20
(2 marks)
Inputs:
none

Outputs:
Example:
2
4
6
8
10
...
"""
i=1
j=0
while j<20:
    j=i*2
    i+=1
    print(j)
