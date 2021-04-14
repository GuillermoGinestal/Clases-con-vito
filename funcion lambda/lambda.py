'''
MAP
'''

values = [1,2,3]

def pow(a):
    return a ** 2

map(pow,values)

print(list(map(pow,values)))

