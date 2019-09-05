n = int(input("Enter a number: "))
for x in range(1, int(n/2)+1):
    if n%x == 0:
        print(x)

'''
Enter a number: 18
1
2
3
6
9
'''
