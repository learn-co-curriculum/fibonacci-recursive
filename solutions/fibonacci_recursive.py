def fibonacci(n):

    # base case
    if n < 2:
        return n
    
    # recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':

    print("Expecting: 0")
    print(fibonacci(0))

    print("")

    print("Expecting: 1")
    print(fibonacci(2))

    print("")

    print("Expecting: 55")
    print(fibonacci(10))

    print("")

    print("Expecting: 1")
    print(fibonacci(1))

    print("")

    print("Expecting: 6765")
    print(fibonacci(20))

# Please add your pseudocode to this file
################################################################################
# if n is less than 2 return n
#
# return last value in sequence + second to last value in sequence
################################################################################

# And a written explanation of your solution
################################################################################
# We can use the same base case as the iterative version: if n is less than 2, just
# return n, since 0 and 1 are the first values in the series. After that we need to
# calculate the next value by adding up the two previous values. If we recurse until
# n equals 0 or 1, we'll hit the base case and start returning values, which can then
# be added together. For example, if we start with n = 2, our recursive call will be
# fibonacci(1) + fibonacci(0). Both sides of the equation will hit the base case. The 
# left side will return 1 and the right side will return 0, resulting in a total of 1.
################################################################################