l = [[1,2],[3,[4,5,[6,7]]]]
output = []

def removeList(l):
	for i in l:
		if type(i) == list:
			removeList(i)
		else:
			output.append(i)

removeList(l)
print output

