# fh=open("xyz.txt","wt")
# content=fh.read()
# print(content)
# fh.close()


with open("xyz.txt","rt") as fh:
    content = fh.read()

print(content)