from django.db import models

# Create your models here.
class Time(models.Model):
    nome = models.CharField(max_length=100)
    ano_fundacao = models.IntegerField()
    pais = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} ({self.cidade} - {self.estado}, {self.pais}) - Fundado em {self.ano_fundacao}"