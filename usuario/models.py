from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    picture = models.ImageField(upload_to='user_fotos/', null=True)

    def __str__(self):
        return self.user.username

    # Retorna o nome completo do usuário
    @property
    def full_name(self):
        return self.user.get_full_name()
    
    def is_active(self):
        return self.user.is_active

    # Retorna a data que o usuário se cadastrou
    @property
    def date_joined(self):
        return self.user.date_joined