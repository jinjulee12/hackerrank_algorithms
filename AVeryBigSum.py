'''
Title     : A Very Big Sum
Domain    : Python
Created   : 04 OCT 2018
'''
#same code with "Title : Simple Array Sum"

get_number = int(input())
get_array = input('Input' + str(get_number) +  'numbers with space')

get_list = get_array.split(' ')

#print(get_number)
#print(get_list)


total = 0
while get_number > 0 :
    number = int(get_list[get_number-1])
    total = total + number
    get_number = get_number - 1
print(total)
