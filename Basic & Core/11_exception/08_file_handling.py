# No text file is present in directory
# If you want to open the file, using "open" method can do this.
#  

try:
    file = open("order.txt", "w")
    file.write("Masala Chai - 2 cups")
finally:
    file.close() # file.__exit__() it will call the dunder in backend.


# Another way to file handling -> it will work as try catch for files
# when you create a file reference like "file" it will create dunder 
# e.g. file.__enter__ it will execute file.__enter__() and when you close this it will be file.__exit__()
with open("order.txt", "w") as file:
    file.write("Ginger tea - 4 cups")

