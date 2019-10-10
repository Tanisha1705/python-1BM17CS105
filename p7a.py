def sumsquared(n): 
    s1 = 0 
    while(n): 
        s1 += (n % 10) * (n % 10) 
        n = int(n / 10) 
    return s1
def checkhappy(n): 
    slow = n
    fast = n 
    while(True): 
        slow = sumsquared(slow) 
        fast = sumsquared(sumsquared(fast)) 
        if(slow != fast): 
            continue 
        else: 
            break
    return (slow == 1)
lp=[]
for i in range(1,1001):
    for j in range(2,i):
        if(i%j)==0 and j not in lp:
            lp.append(j)
f1=open("sprime.txt","w")
for i in lp:
    f1.write(str(i))
    f1.write("\n")
f1.close()
f2=open("shappy.txt","w")
for i in range(1,1001):
    if(checkhappy(i)):
        f2.write(str(i))
        f2.write("\n")
f2.close()
common=[]
f3=open("sprime.txt","r")
f4=open("shappy.txt","r")
for i in f3.readlines():
    f4.seek(0)
    for j in f4.readlines():
        if int(i)==int(j) and int(i) not in common:
            common.append(int(i))
print(common)

 
        
