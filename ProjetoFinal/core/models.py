from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome    


class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):  
    marca = models.ForeignKey(Marca)
    placa = models.CharField(max_length=7)
    proprietario = models.ForeignKey(Pessoa)
    cor = models.CharField(max_length=15)
    observacoes = models.TextField()
    
    def __str__(self):
        return self.marca.nome + ' - ' + self.placa 


class Parametros(models.Model):
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self):
        return 'Parametros Gerais'


class MovRotativo(models.Model):
    checkin = models.DateTimeField(auto_now=False)
    checkout = models.DateTimeField(auto_now=False, null=True, blank=True)
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    veiuclo = models.ForeignKey(Veiculo)
    pago = models.BooleanField(default=False)

    def __str__(self):
        return self.veiuclo.placa 
