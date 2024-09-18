# open, read and write mode

# read - "r"
# write - "w"

# f = open ("demo.txt", "r")
# content = f.read()
# print(content)
# f.close()


f = open ("demo.txt", "w")
f.write ("I am learning file handling")

f.close()