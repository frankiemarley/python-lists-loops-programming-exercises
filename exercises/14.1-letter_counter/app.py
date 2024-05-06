par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}

# Your code here
par = par.lower()
for i in par:
    if i != " ":
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1


print(counts)
