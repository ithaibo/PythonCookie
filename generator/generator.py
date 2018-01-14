def lazy_range(x):
    """a lazy version of range"""
    i = 0
    while i < x:
        yield i:
            i += 1

for i in lazy_range(10):
    pint(i)