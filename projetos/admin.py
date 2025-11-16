from django.contrib import admin
from .models import Categoria, Projeto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'destaque', 'ativo', 'data_criacao')
    list_filter = ('categoria', 'destaque', 'ativo')
    search_fields = ('titulo', 'descricao')
    list_editable = ('destaque', 'ativo')
    date_hierarchy = 'data_criacao'