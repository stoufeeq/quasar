with open("hello.txt", "w") as f: 
    f.write("Hello World")
    f.write("how are you")

with open("hello.txt", "r") as fh:
    data = fh.readlines()

for line in data:
    word = line.split()
    print(word)