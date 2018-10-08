'''
Title     : Staircase
Domain    : Python
Created   : 08 Oct 2018
'''

#Wrong!!!!

n = int(input())
a = 1
while n > 0 :
    print(' '*(n-a), '#'*a)
    n -= 1
    a += 1
