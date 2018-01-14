even_numbers = [x for x in range(5) if x % 2 == 0]
print 'even numbers in range 5:'
print even_numbers

squares = [x*x for x in range(5)]
print 'square numbers in range 5:'
print squares

even_squares = [x * x for x in even_numbers]
print 'even square numbers in even numbers:'
print even_squares