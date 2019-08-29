def binarySearch(lst, l, r, x):
    while l <=r:
        mid = int(l + (r - l) / 2)
        if lst[mid] == x:
            return True
        elif lst[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return False

arr = [int(i) for i in input("Enter numbers in the list: ").split()]
x = int(input("Enter number to be found: "))
search = binarySearch(arr, 0, len(arr)-1, x)
if search:
    print("Number found")
else:
    print("Number not found")


'''
Enter numbers in the list: 1 2 3 4 5
Enter number to be found: 1
Number found

Enter numbers in the list: 6 7 8 9 10
Enter number to be found: 1
Number not found
'''
