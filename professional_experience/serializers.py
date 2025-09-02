from rest_framework import serializers
from .models import ProfessionalExperience

class ProfessionalExperienceSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo ProfessionalExperience.
    """
    class Meta:
        model = ProfessionalExperience
        fields = '__all__'
        read_only_fields = ('user',) # O usuário será definido pela view