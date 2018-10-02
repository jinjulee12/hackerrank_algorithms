'''
Title     : Loops
Domain    : Python
Created   : 02 Oct 2018
'''

N = int(input('''Write any number 1~20'''))

if 0 < N < 21 :
    while N > 0 :
        print((N-1)**2)
        N -= 1
        
#Have to inverse order of the result 
