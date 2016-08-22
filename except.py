try:
	print(int('x'))
	print(int('2'))
except:
	print('Nao foi possivel realizar a conversao')
else: # No excepetion
	print('Todo os itens foram convertidos')
finally: # Always
	print('Conversao terminada')	
