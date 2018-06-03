for i in range(4, 10):
    print(i)
else:
    print('Fim loop')

list1 = ['Maca', 'Banana', 'Melao']
list2 = ['Tomate', 'Cebola', 'Cenora']

for i, j in zip(list1, list2):
    print(i, j)

for i,j in enumerate(list1):
    print(i, j)