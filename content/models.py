from django.db import models
from django.utils.text import slugify

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)
    published = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.question



# Nuevo modelo para favoritos
class FavoriteItem(models.Model):
    TYPE_CHOICES = [
        ("serie", "Serie"),
        ("anime", "Anime"),
        ("juego", "Juego"),
    ]
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=10, choices=TYPE_CHOICES)
    imagen = models.ImageField(upload_to="favorite_items/")
    resumen = models.CharField(max_length=300)
    descripcion = models.TextField()
    palabras_clave = models.CharField(max_length=200)
    año_lanzamiento = models.IntegerField()
    link_externo = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} ({self.tipo})"


# Modelo para mensajes de contacto
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
