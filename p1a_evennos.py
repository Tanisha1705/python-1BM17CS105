arr = []
n = int(input("Enter no of elements"))
for x in range(0, n):
    arr.append(int(input("INPUT ->")))
even = []
for x in arr:
    if x%2 == 0:
        even.append(x)

print("ORIGINAL ARRAY: ", arr)
print("EVEN ARRAY: ", even)

'''
Enter no of elements5
INPUT ->1
INPUT ->2
INPUT ->3
INPUT ->4
INPUT ->5
ORIGINAL ARRAY:  [1, 2, 3, 4, 5]
EVEN ARRAY:  [2, 4]
'''
