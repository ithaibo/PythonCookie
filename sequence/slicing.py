months =[
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

print months[-3 : -1]
print months[0 : 2]
print months[-1 : -3] # []
print months[-3:]
print months[0:3]

# step 2
print months[::2]
# step -2
print months[::-2]
# step -1
print months[-1 : -3 : -1]

# slicing adding
print [1,2,3] + [4,5,6]