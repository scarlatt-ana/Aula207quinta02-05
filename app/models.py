from django.db import models

class Produto (models.Model):
    nome = models.CharField (max_length = 100)
    preco = models.DecimalField (decimal_places= 2, max_digits=100, default=0)
    descricao = models.TextField (blank= True, null=True)
    em_estoque = models.BooleanField (default=True)

    def __str__(self):
        return self.nome

class Pedido (models.Model): 
    pagamento_a_vista= 'av'
    parcela_2x = 'p2' 
    parcela_3x = 'p3'
    parcela_4x = 'p4'
    parcela_5x = 'p5'

    pagamento_opcoes= [
        (pagamento_a_vista, 'pagamento a vista'),
        (parcela_2x, 'parcela duas vezes'),
        (parcela_3x, 'parcela tres vezes'),
        (parcela_4x, 'parcela quatro vezes'),
        (parcela_5x, 'parcela cinco vezes'),
        

    ]


    nome = models.CharField (max_length =  100)
    email = models.EmailField ()
    endereco = models.CharField (max_length = 150)
    cartao = models.IntegerField ()
    pagamento = models.CharField (max_length = 2, choices= pagamento_opcoes, default=pagamento_a_vista)

    def __str__(self):
        return self.nome





# Create your models here.
