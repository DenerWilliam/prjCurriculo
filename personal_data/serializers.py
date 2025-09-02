from rest_framework import serializers
from .models import PersonalData

class PersonalDataSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo PersonalData.
    Ele converte as instâncias do modelo em dados JSON para a API e valida
    os dados recebidos para criação ou atualização.
    """
    class Meta:
        model = PersonalData
        fields = ['full_name', 'phone', 'email', 'linkedin_url', 'github_url', 'city', 'state']
