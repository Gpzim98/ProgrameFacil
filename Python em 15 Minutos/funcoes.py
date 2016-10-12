def soma(total, num=2):
	return total + num

print soma(1, 10)

print soma(total=10)

d ={'total': 1, 'num': 4}

print soma(**d)


def calc(val1, val2, func):
	return func(val1, val2)
	
def mul(a, b):
	return a * b


opt = 'mul'

if opt == 'soma':
	print calc(10, 7, soma)
elif opt == 'mul':
	print calc(10, 2, mul)
