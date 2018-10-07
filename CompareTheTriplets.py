


a_input = input()
b_input = input()

a = a_input.split(' ')
b = b_input.split(' ')

al = [int(a[0]), int(a[1]), int(a[2])]
bl = [int(b[0]), int(b[1]), int(b[2])]

alice = 0
bob = 0
x= 0
while x < 3:
    if al[x] > bl[x]:
        alice += 1
    
    elif al[x] < bl[x]:
        bob += 1    
    x += 1
print(alice, bob)
