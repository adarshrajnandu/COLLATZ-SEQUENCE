# This code performs the simplest imposible math problem
# COLLATZ SEQUENCE

print('Please enter the number')

num = int(input())

def collatz(n):
    global t
    if n % 2 == 0:
        t = 'even'
    else:
        t = 'odd'
    return(t)

i = 0

while i != 1:    # this will loop unit we get the number 1
    collatz(num)
    
    if t == 'even':
        num = num // 2
    else:
        num = 3 * num + 1
    
    i = num
    print(num)
