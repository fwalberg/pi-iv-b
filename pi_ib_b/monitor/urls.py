from django.urls import path
from . import views

urlpatterns = [
    path('api/status/', views.verificar_status_json, name='status_api'),
    path('status/', views.vericar_status_web, name='status_web')

]
