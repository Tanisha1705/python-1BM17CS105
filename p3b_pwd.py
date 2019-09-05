import random
smallchar = 'abcdefghijklmnopqrstuvwxyz'
bigchar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
splchar = '!@#$&%*^()'
number = '1234567890'
ctr = [0,0,0,0]
def choose(stn):
    return stn[random.randint(0, len(stn)-1)]

length = random.randint(8, 15)
pwd = ''
for x in range(0, length):
    while True:
        avg = sum(ctr)/4
        choice = random.randint(0,3)
        if ctr[choice] <= avg:
            break
    if(choice == 0):
        ch = choose(smallchar)
    elif(choice == 1):
        ch= choose(bigchar)
    elif(choice == 2):
        ch = choose(splchar)
    else:
        ch = choose(number)
    ctr[choice] += 1
    pwd += ch

print(pwd)
