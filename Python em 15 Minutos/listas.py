a = ['texto', (1,2), [2,3], 1, 2, 2, 4]

a.append(4)

print a

a[2] = 'Texto'

print a[1]

print a.count((1,2))


print a.index(4)

a.insert(0, 5)
print a

a.reverse()
print a

a.sort()
print a