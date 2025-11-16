from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Projeto, Categoria

def home(request):
    """
    View da página inicial com slider de projetos em destaque
    """
    projetos_destaque = Projeto.objects.filter(destaque=True,ativo=True)[:3]
    return render(request, 'projetos/home.html', {
        'projetos_destaque':projetos_destaque
    })


def lista_projetos(request):
    """
    View de listagem de projetos com filtro por categoria
    """
    categoria_id = request.GET.get('categoria')
    projetos = Projeto.objects.filter(ativo=True) #filtro na base
    
    if categoria_id:
        projetos = projetos.filter(categoria_id=categoria_id)
        
    categorias = Categoria.objects.all() #recupero tudo de Categoria da base
    
    return render(request, 'projetos/lista_projetos.html', {
        'projetos':projetos,
        'categorias': categorias,
        'categoria_selecionada': categoria_id
    })


def detalhes_projeto(request, projeto_id):
    """
    View de detalhes de um projeto específico
    """
    projeto = get_object_or_404(Projeto,id=projeto_id,ativo=True)
    projetos_relacionados = Projeto.objects.filter(
        categoria = projeto.categoria,
        ativo = True
    ).exclude(id=projeto.id)[:3]
    
    return render(request, 'projetos/detalhes_projeto.html',{
        'projeto':projeto,
        'projetos_relacionados':projetos_relacionados
    })


@login_required
def meus_projetos(request):
    """
    View protegida - apenas usuários autenticados podem acessar
    Mostra estatísticas e gestão de projetos
    """
    total_projetos = Projeto.objects.count()
    projetos_ativos = Projeto.objects.filter(ativo=True).count()
    projetos_destaque = Projeto.objects.filter(destaque=True).count()
    projetos_recentes = Projeto.objects.all()[:5]
    
    return render(request, 'projetos/meus_projetos.html', {
        'total_projetos':total_projetos,
        'projetos_ativos': projetos_ativos,
        'projetos_destaque': projetos_destaque,
        'projetos_recentes': projetos_recentes
    })
    