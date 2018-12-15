1. 并行迭代

2. 循环中的else
``` python
from math import sqrt
for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print n
        break
else:
    print "didn't find it"
# didn't find it
```

3. 列表推导式
``` python
girls = ['alice', 'bernice', 'clarice']
boys  = ['chris', 'arnold', 'bob']
matched = [b+' + '+g for b in boys for g in girls if b[0] == g[0]]
```