from django.db import models
#https://docs.djangoproject.com/en/1.11/ref/models/fields/#model-field-types


class Departamento(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class CPF(models.Model):
    numero = models.CharField(max_length=15)
    data_exp = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.numero


class Empregado(models.Model):
    nome = models.CharField(max_length=70, null=False)
    endereco = models.CharField(max_length=200, blank=False, null=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    idade = models.IntegerField()
    email = models.EmailField()
    cpf = models.OneToOneField(CPF, blank=True, null=True)
    departamentos = models.ManyToManyField(Departamento, blank=True)
    foto = models.ImageField(upload_to='cliente_fotos')

    def __str__(self):
        return self.nome


class Telefone(models.Model):
    numero = models.CharField(max_length=20)
    descricao = models.CharField(max_length=80)
    empregado = models.ForeignKey(Empregado)

    def __str__(self):
        return self.descricao + ' - ' + self.numero
