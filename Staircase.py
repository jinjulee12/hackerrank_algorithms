'''
Title     : Staircase
Domain    : Python
Created   : 08 Oct 2018
'''

n = int(input())
a = 1

while n > 0 :
    print(' '*(n-1),'#'*a)
    n -= 1
    a += 1
