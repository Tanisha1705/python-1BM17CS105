class match:
    def checkmatch(self, inp):
        lst = []
        dict = {']' : '[', '}' : '{', ')': '('}
        for x in inp:
            if x in '({[':
                lst.append(x)
            elif x in ')}]':
                if dict[x] != lst.pop():
                    return 'Invalid'
        if len(lst) == 0:
            return 'Valid'
        return 'Invalid'

inp = input("Enter str: ")
print(match().checkmatch(inp))

    
