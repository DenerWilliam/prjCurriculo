from django.db import models
from users.models import User

class PersonalData(models.Model):
    """
    Modelo para armazenar os dados pessoais do currículo.
    """
    # Usamos OneToOneField para garantir que cada usuário tenha um e apenas um currículo.
    # related_name permite acessar os dados pessoais a partir do objeto User.
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='personal_data')
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    linkedin_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return f"Dados de {self.full_name}"
