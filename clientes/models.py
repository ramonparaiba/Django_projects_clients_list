from django.db import models

sexo_Choices = (
    ('m', 'Masculino'),
    ('f', 'Feminino'),
    ('n', 'Não informar')
)

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=1, choices = sexo_Choices)
    email = models.EmailField(blank=True, null = True)

    def __str__(self):
        return self.nome
    
