from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class TestResult(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    respuestas = models.JSONField()

    def __str__(self):
        return f"Test de {self.usuario.username} - {self.fecha.strftime('%d/%m/%Y')}"

class IkigaiResult(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    respuestas = models.JSONField()

    def __str__(self):
        return f"IKIGAI de {self.usuario.username} - {self.fecha.strftime('%d/%m/%Y')}"

class Carrera(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    area = models.CharField(max_length=50)  # Ej: salud, tecnología, social
    habilidades_clave = models.TextField()  # Separadas por coma

    def __str__(self):
        return self.nombre
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_de_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()