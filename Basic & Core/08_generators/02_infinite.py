# It is usefull for streams / constantly getting log values
# Use carefully, it can drain your memory

# It will create infinite loop.
def infinite_chai():
    count = 1
    while True:
        yield f"Refil #{count}"
        count += 1

refill = infinite_chai()

# Using for loop to get values. _ underscore used for to not define any variable it is not usefull
for _ in range(3):
    print(next(refill))

print("\n---------\n")

user2 = infinite_chai()
for _ in range(6):
    print(next(user2))

