filename = 'learning_python.txt'

#Reading in the entire file:
with open(filename) as f:
    contents = f.read()
print(contents)


#Looping over the file object:
with open(filename) as f:
    for line in f:
        print(line.rstrip())

#Storing the lines in a list:
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())