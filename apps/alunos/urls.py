from django.urls import path
from apps.alunos import views


urlpatterns = [
    path("alunos", views.alunos, name="alunos")
]
