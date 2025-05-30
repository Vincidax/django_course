# create a function
def print_x_times(parameter, loop_amount = 5):
    counter = 0
    while counter < loop_amount:
        print(counter, parameter)
        counter += 1
    return 'something else'

# call
print('print')
test = print_x_times('test')
print(test)