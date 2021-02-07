
# BINARY SEARCH #
def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) //2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint

        elif item < midpoint_value:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1

    return None

sequence_a = [2,4,6,8,9,23,25,32]
item_a = 25

print(binary_search(sequence_a, item_a))

# loops #

# basic array 
nums = [1,2,3,4,5]
# basic for loop
for num in nums:
    print(num)

# for loop with conditionals

# for loop with a break statement, when you hit the break statement you will
# break out of the for loop
for num in nums:
    if num == 3:
        print("found!!!")
        break
    print(num)

    # for loop with a continue statement, when you hit the continue statement 
    # the loop will com=ntinue on after
    for num in nums:
        if num == 3:
            print("found!!")
            continue
        print(num)









        






            