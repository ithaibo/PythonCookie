#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# while condiftion :
#      //do something

# words = ['this', 'is', 'an', 'ex', 'parrot']
# for word in words:
    # print word

# numbers = range(0, 10)
# for num in numbers:
    # print num

from math import sqrt
for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print n
        break
else:
    print "didn't find it"

girls = ['alice', 'bernice', 'clarice']
boys  = ['chris', 'arnold', 'bob']
matched = [b+' + '+g for b in boys for g in girls if b[0] == g[0]]
print str(matched)