file = open("text_1.txt", "w")

file.write("My super text")
for line in file:
    print(line)
print(file.read())
print(file.readline())
print(file.read(4))
file.close()

with open("text_1.txt", "r") as file:
    print(file.read())
with open("text_1.txt", "r") as file:
    print(file.read())
    file.write('some dummy text')
    print(file.read())
file.close()
