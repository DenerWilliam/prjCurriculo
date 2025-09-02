from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import PersonalData
from .serializers import PersonalDataSerializer

class PersonalDataAPIView(APIView):
    """
    View para gerenciar os dados pessoais do currículo.
    Permite buscar, criar e atualizar os dados do usuário logado.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, user):
        """Helper para buscar o objeto PersonalData do usuário logado."""
        try:
            return PersonalData.objects.get(user=user)
        except PersonalData.DoesNotExist:
            return None

    def get(self, request):
        """Retorna os dados pessoais do usuário logado."""
        personal_data = self.get_object(request.user)
        if personal_data:
            serializer = PersonalDataSerializer(personal_data)
            return Response(serializer.data)
        return Response({'detail': 'Dados pessoais não encontrados.'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        """Cria os dados pessoais para o usuário logado."""
        personal_data = self.get_object(request.user)
        if personal_data:
            return Response({'detail': 'Dados pessoais já existem.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PersonalDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        """Atualiza os dados pessoais do usuário logado."""
        personal_data = self.get_object(request.user)
        if not personal_data:
            return Response({'detail': 'Dados pessoais não encontrados para atualização.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PersonalDataSerializer(personal_data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)