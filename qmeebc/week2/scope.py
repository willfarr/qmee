## Try this first

_a_global = 10

#so this variable is available outside the function made below

def a_function():
    _a_global = 5
    _a_local = 4
    print("Inside the function, the value is ", _a_global)
    print("Inside the function, the value is ", _a_local)
    return None
#these variables are only available inside the function
a_function()

print("Outside the function, the value is ", _a_global)


## Now try this

_a_global = 10

def a_function():
    global _a_global
    _a_global = 5
    _a_local = 4
    print("Inside the function, the value is ", _a_global)
    print("Inside the function, the value is ", _a_local)
    return None

a_function()
print("Outside the function, the value is", _a_global)

# adding the 'global' inside the function made it global everywhere, and replaced the original
