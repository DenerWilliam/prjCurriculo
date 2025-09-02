from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Modelo de usuário customizado que herda de AbstractUser.
    Permite adicionar campos extras no futuro sem ter que refazer as migrações.
    """
    # Adicione campos customizados aqui, se necessário.
    # Por enquanto, o modelo padrão do Django já é suficiente.
    pass
