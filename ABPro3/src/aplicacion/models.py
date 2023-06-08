from django.db import models

class Clientes(models.Model):
    name =models.CharField(max_length=100)
    edad =models.SmallIntegerField()
    email =models.EmailField()
    ciudad =models.CharField(max_length=100)
    telefono =models.SmallIntegerField()
    
    def __str__(self):
        return self.name