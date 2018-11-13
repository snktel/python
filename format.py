n = 11
f = 1.2345678
s = "computer"

print("my number is {:d}".format(n))
print("my number is {:b}".format(n))

print("{:f}".format(f))
print("{:.3f}".format(f))
print("{:011.3f}".format(f))

print("{0} {1} {2}".format(n,f,s))

print("{name} own(s) {amount} of {object}".format(
    name = "Sergey",
    amount = 5,
    object = "mangos!"
))
