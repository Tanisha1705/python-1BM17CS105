def fib(n):  
   if n <= 1:  
       return n
   else:  
       return(fib(n-1) + fib(n-2))  

n = int(input("Enter no of fibonacci elements "))    
for i in range(n):  
    print(fib(i))

'''
Enter no of fibonacci elements 6
0
1
1
2
3
5
'''
