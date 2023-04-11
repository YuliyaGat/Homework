#Task1 detect the number of local variables declared in a function

def my_function(n):
    q = 1
    w = [1,2,3]
    my_string = 'Hello!'
print(my_function.__code__.co_nlocals-my_function.__code__.co_argcount)



