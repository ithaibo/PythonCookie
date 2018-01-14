even_numbers = [x for x in range(5) if x % 2 == 0]
# print 'even numbers in range 5:'
# print even_numbers

squares = [x*x for x in range(5)]
# print 'square numbers in range 5:'
# print squares

even_squares = [x * x for x in even_numbers]
# print 'even square numbers in even numbers:'
# print even_squares

square_dict = {x : x * x for x in range(5)}
# print 'square dictionary in range 5:'
# print square_dict

zeros = [0 for _ in even_numbers]
# print zeros

pairs = [(x,y)
            for x in range(10)
            for y in range(x+1, 10)]
            
print pairs