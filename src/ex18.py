# this one is like your scripts with argv
def print_three(*argv):
    arg1, arg2, arg3 = argv
    print(f"arg1: {arg1}; arg2: {arg2}; arg3: {arg3}")

# ok, that *args is actually pointless, we can just do this:
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}; arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_nothing():
    print("I got nothin'.")

print_three("huy", "truong", "duc")
print_two_again("Huy", "Truong")
print_one("first")
print_nothing()