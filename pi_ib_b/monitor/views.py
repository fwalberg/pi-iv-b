from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import JsonResponse
import requests

url = "http://146.235.37.219:8080"

@login_required
def verificar_status_json(request):
    try:
        response = requests.get(url)
        status = response.status_code

        if status == 200:
            return JsonResponse({
                "url": url,
                "site_status": "Site On-line",
                "http_code": status
            })
        else:
            return JsonResponse({
                "url": url,
                "status": "SITE OFF-LINE!",
                "http_code": status
            })
    except requests.exceptions.RequestException as e:
        return JsonResponse({
            "status": "Erro ao verificar o site!",
            "error": str(e)
        })

@login_required
def vericar_status_web(request):
    status_site = "Nao verificado"
    status_code = None

    try:
        response = requests.get(url)
        status_code = response.status_code

        if status_code == 200:
            status_site = "Site On-line"
        else:
            status_site = f"SITE OFF-LINE! - HTTP STATUS: {status_code}"
    except requests.exceptions.RequestException as e:
        status_site = f"Erro ao verificar o site! - {str(e)}"

    return render(request, 'status_site.html', {
        'url': url,
        'status': status_site,
        'http_code': status_code
    })


@login_required
def cadastro_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Lógica após login bem-sucedido
            return redirect('pagina_sucesso')
        else:
            # Tratamento de credenciais inválidas
            return render(request, 'login.html', {'error': 'Credenciais inválidas'})

    return render(request, 'login.html')