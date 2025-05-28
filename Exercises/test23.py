a = {
    1: "one",
    2: "three"
}

b = {
    2: "two"
}

c = {
    3: "three"
}

print(a)
# {1: 'one', 2: 'three'}

print(b)
# {2: 'two'}

a.update(b)
print(a)
# {1: 'one', 2: 'two'}

a.update(c)
print(a)
# {1: 'one', 2: 'two', 3: 'three'}
