'''
Title     : Print Fuction
Domain    : Python
Created   : 03 Oct 2018
'''

n = input()

if n.isnumeric() :
    N = int(n)
    rangeN = range(1,N+1)
    for i in rangeN :
        print(i, end="")
else :
    print('Input INTEGER!!!')
