from django.db import models
from users.models import User

class ProfessionalExperience(models.Model):
    """
    Modelo para armazenar a experiência profissional do currículo.
    Um usuário pode ter várias experiências.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='professional_experiences'
    )
    job_title = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    is_current = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Experiência Profissional"
        verbose_name_plural = "Experiências Profissionais"

    def __str__(self):
        return f"{self.job_title} em {self.company_name}"
