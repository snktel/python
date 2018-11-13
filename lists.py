numbers = [5, -6, 2, 4, -5, 1]
names = ["Heather", "Micah", "Jane"]

print(names[0])
print(names[1])
print(names[2])
#print(names[4])

print(names)
del names[1]
print(names)

mystr = "Hello World"
print(mystr[0])
print(mystr[6])

alpha = ["a", "b", "c", "d"]
# alpha.append("e")
alpha = alpha + ["f", "g"]

print(alpha)
d_index = alpha.index("d")
print("d_index: " + str(d_index))
del alpha[d_index]
print(alpha)

alpha.remove("c")
print(alpha)
