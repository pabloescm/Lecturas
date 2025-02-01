from django.db import models

class Lectura(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=200)
    fecha = models.DateField(auto_now_add=True)
    resumen = models.TextField()

    def __str__(self):
        return self.titulo