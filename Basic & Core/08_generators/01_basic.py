# Generators --> We are generating things, It fetched the value one by one
# NORMAL FUNCTION --> in the function or in the loop get the result immediately, everything is loaded in the memory, in the loop or other functions
# Yeild pauses the function and resume the function on then next call, where extactly where it stops

def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Elaichi Chai"

stall = serve_chai()
# print(stall) # <generator object serve_chai at 0x00000117A4BD5480>

for cup in stall:
    print(cup)


# Regular function
def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

# Generator function
def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai_gen()
print(chai)         # <generator object get_chai_gen at 0x0000025369175480>
print(next(chai))   # Cup 1
print(next(chai))   # Cup 2
print(next(chai))   # Cup 3
print(next(chai))   # Error StopIteration

