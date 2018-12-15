from functools import partial

def exp(base, power):
    return base ** power

tow_to_the = partial(exp, 2)
print "3 power of 2 is ", tow_to_the(3)


square_of = partial(exp, power = 2)
print "square of 3 is ", square_of(3)


def double(x):
    return 2*x

xs = [1,2,3,4]
print 'xs is       ', xs
# twice_xs = [double(x) for x in xs]
twice_xs = map(double, xs)
print 'twice_xs is ', twice_xs

list_double = partial(map, double)
twice_xs = list_double(xs)
print 'twice_xs is ', twice_xs