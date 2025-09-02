from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import ProfessionalExperience
from .serializers import ProfessionalExperienceSerializer

class ProfessionalExperienceListCreateView(generics.ListCreateAPIView):
    """
    View para listar todas as experiências profissionais do usuário
    e permitir a criação de uma nova experiência.
    """
    serializer_class = ProfessionalExperienceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Retorna apenas as experiências profissionais do usuário autenticado.
        """
        user = self.request.user
        return ProfessionalExperience.objects.filter(user=user).order_by('start_date')

    def perform_create(self, serializer):
        """
        Associa automaticamente a nova experiência ao usuário autenticado.
        """
        serializer.save(user=self.request.user)


class ProfessionalExperienceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View para visualizar, atualizar ou excluir uma experiência profissional específica.
    """
    serializer_class = ProfessionalExperienceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Retorna apenas as experiências profissionais do usuário autenticado.
        """
        user = self.request.user
        return ProfessionalExperience.objects.filter(user=user)
