filename = 'learning_python.txt'

with open(filename) as f:
    lines = f.readlines()

for line in lines:
    line = line.rstrip()
    print(line)
    print(line.replace('Python', 'Java'))
