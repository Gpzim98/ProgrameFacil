class Dog:
    name = 'rex'

    def __init__(self):
        self.name = 'Lulu'

obj = Dog()
obj.name = 'Toto'
print obj.name

class Doc(object):
	name = ''
	def __init__(self, name):
		self.name = name

a = Doc('Ruf')
print a.name


class Dog(object):
        def __init__(self):
                print 'Object instaciate'

        def latir(self, ofthen):
                print 'Au! ' * ofthen

class SaoBernardo(Dog):
        def latir(self, ofthen = 1):
                print 'Woof! ' * ofthen

c = Dog()
c.latir(10)
