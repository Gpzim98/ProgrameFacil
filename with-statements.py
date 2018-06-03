f = open('texto.txt')

texto = f.read()

for linha in texto.split('\n'):
    print(linha)

f.close()

f = open('texto.txt')

for linha in f.read().split('\n'):
    print(linha)

f.close()

with open('texto.txt') as f: # __enter__()
    for linha in f:
        print(linha)

# __exit__()    
