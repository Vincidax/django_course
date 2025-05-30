# if statements
# if 5 < 4:
#     print("correct statement")
# print('test')

#while loop
# counter = 0
# while counter <= 10:
#     print(counter)
#     counter += 1
#     if counter == 5:
#         print('counter is 5')
# print('while loop has finished')

#for loop

# test_list = {1:2, 3:4, 5:6}
# for x in test_list.items():
#     print(x[1])

# truthy and falsy:
# if 'l':
#     print('truly')
# else:
#     print('falsy')

a_list = [1,2,3,4,5]

for x in a_list:
    if x == 5:
        counter = 0
        while counter <= 5:
            print('last item')
            counter += 1
    
    elif x == 2:
        print('the value is 2')

    else:
        print('the value is not 2')