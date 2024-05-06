the_bools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

# Your code here

def format_bools(list1):
    if list1 == 0:
        return 'woko'
    else:
        return 'wiki'


result = list(map(format_bools, the_bools))

print(result)
