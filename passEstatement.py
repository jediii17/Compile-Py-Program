# function takes in a number and prints whether it is positive, negative, or zero.
def my_function(x):
    if x > 0:
        print("Positive number")
    elif x < 0:
        print("Negative number")
    else:
        print("no output")
        pass


my_function(1)   # Positive number
my_function(-1)  # Negative number
my_function(0)   # No output

# In this example, the function my_function takes an argument x
# and prints whether it is a positive or negative number. If x is
# zero, the pass statement is executed and no output is produced.
