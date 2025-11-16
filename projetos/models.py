from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(blank=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Categorias"


class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='projetos')
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    url_projeto = models.URLField(blank=True, null=True)
    destaque = models.BooleanField(default=False, help_text="Aparecerá no slider da home")
    data_criacao = models.DateField(auto_now_add=True)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['-data_criacao']
        verbose_name_plural = "Projetos"