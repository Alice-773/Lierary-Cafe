from django.db import models

class Livro(models.Model):
    
    CATEGORIA_CHOICES = [
        ('FICCAO', 'Ficção'),
        ('ROMANCE', 'Romance'),
        ('TECNICO', 'Técnico'),
        ('BIOGRAFIA', 'Biografia'),
        ('OUTROS', 'Outros'),
    ]

    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    
    
    categoria = models.CharField(
        max_length=50,
        choices=CATEGORIA_CHOICES,
        default='OUTROS'
    )
    
    isbn = models.CharField(max_length=20)
    ano = models.IntegerField()
    quantidade = models.IntegerField(default=1)
    disponivel = models.BooleanField(default=True)

    
    emprestado_para = models.CharField(max_length=100, blank=True, null=True)
    data_emprestimo = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.titulo