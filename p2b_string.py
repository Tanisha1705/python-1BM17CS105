inp = input("Enter a string: ")
lst = inp.split(" ")
rev = ""
for x in lst:
    print(x[::-1], end=' ')
    rev = x + " " + rev
print()
print(rev)

'''
Enter a string: Welcome to BMSCE
emocleW ot ECSMB 
BMSCE to Welcome
'''
