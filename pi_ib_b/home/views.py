from django.shortcuts import render

def home_page(request):
    context = {
        'nome_projeto': 'Projeto Integrador IV-B'
    }
    return render(request, 'index.html', context)