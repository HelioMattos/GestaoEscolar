from django.db import models

class Disciplina(models.Model):
    nome_disciplina = models.CharField(max_length=100)
    nome_professor = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_disciplina