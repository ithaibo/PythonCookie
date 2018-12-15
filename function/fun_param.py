# function as paramters
def apply_to_one(fun):
    return fun(1)

def print_dict(**params):
    print params
print_dict(x=1,y=2,z=3)

def print_tuple(*params):
    print params
print_tuple(1, 2, 3)

def print_1(x, y, z=3, *tp, **dt):
    print x, y, z
    print tp
    print dt
print_1(1,2,3, 4, 5, 6, foo=8, bar=9)
print_1(1, 2)