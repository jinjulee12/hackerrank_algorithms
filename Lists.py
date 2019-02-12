
'''
Title     : Lists
Domain    : Python
Created   : 12 FEB 2019
'''

if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        tmp_str = input()
        split_str = tmp_str.split(" ")
        cmd = split_str[0]
        
        if len(split_str) == 3:
            
            a = int(split_str[1])
            b = int(split_str[2])
            #cmd == "insert":
            arr.insert(a,b)
        
        elif len(split_str) == 2: 
        
            a = int(split_str[1])
            
            if cmd == "remove":
                arr.remove(a)
            elif cmd == "append":
                arr.append(a)
        
        else :
        
            if cmd=="print":
                print(arr)
            elif cmd == "sort":
                arr.sort()
            elif cmd == "pop":
                arr.pop()
            else:
                arr.reverse()
            
