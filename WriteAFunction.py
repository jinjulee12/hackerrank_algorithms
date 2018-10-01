'''
Title     : Write a function
Domain    : Python
Created   : 01 Oct 2018
'''

#Checking if the input year is a leap year or not with roop function

x = 0
while x < 5 : 
    input_year = int(input("Write down any year: "))

    if input_year % 4 == 0 :
        if input_year % 100 == 0 :    
            if input_year % 400 == 0 :
                print('True')
            else :
                print('False')
        else :
            print('True')
    else :
        print('False')
    x += 1
