lista = ['Joao', 'Maria', 'Jose']

procurado = 'Pedro'

print(lista.count(procurado))
#print(lista.index(procurado))

for pessoa in lista:
	if pessoa == procurado:
		print('Encontrado')
		break
else: # No break accurs
	print('Não encontrado')