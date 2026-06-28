from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm
from django.db.models import Q 
from django.contrib.auth.decorators import login_required

@login_required
def lista_livros(request):
    
    termo_busca = request.GET.get('busca', '')
    categoria_filtrada = request.GET.get('cat', '')
    
    livros = Livro.objects.all()
    
   
    if termo_busca:
        livros = livros.filter(
            Q(titulo__icontains=termo_busca) | Q(autor__icontains=termo_busca)
        )
        
   
    if categoria_filtrada:
        livros = livros.filter(categoria=categoria_filtrada)
        
    
    contagem_categorias = {
        'FICCAO': Livro.objects.filter(categoria='FICCAO').count(),
        'ROMANCE': Livro.objects.filter(categoria='ROMANCE').count(),
        'TECNICO': Livro.objects.filter(categoria='TECNICO').count(),
        'BIOGRAFIA': Livro.objects.filter(categoria='BIOGRAFIA').count(),
        'OUTROS': Livro.objects.filter(categoria='OUTROS').count(),
        'TOTAL': Livro.objects.count(),
    }
        
    return render(
        request,
        'livros/lista.html',
        {
            'livros': livros,
            'termo_busca': termo_busca,
            'categoria_filtrada': categoria_filtrada, 
            'contagem': contagem_categorias 
        }
    )

@login_required
def criar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else:
        form = LivroForm()

    return render(
        request,
        'livros/form.html',
        {'form': form}
    )

@login_required
def editar_livro(request, pk):
    livro = get_object_or_404(
        Livro,
        pk=pk
    )

    if request.method == 'POST':
        form = LivroForm(
            request.POST,
            instance=livro
        )
        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else:
        form = LivroForm(
            instance=livro
        )

    return render(
        request,
        'livros/form.html',
        {'form': form}
    )

@login_required
def excluir_livro(request, pk):
    livro = get_object_or_404(
        Livro,
        pk=pk
    )

    if request.method == 'POST':
        livro.delete()
        return redirect('lista_livros')

    return render(
        request,
        'livros/excluir.html',
        {'livro': livro}
    )

@login_required
def home(request):
    total_livros = Livro.objects.count()

    # O teu modelo usa a propriedade 'disponivel', que mapeia perfeitamente para as nossas estatísticas!
    disponiveis = Livro.objects.filter(
        disponivel=True
    ).count()

    indisponiveis = Livro.objects.filter(
        disponivel=False
    ).count()

    return render(
        request,
        'livros/home.html',
        {
            'total_livros': total_livros,
            'disponiveis': disponiveis,
            'indisponiveis': indisponiveis,
        }
    )