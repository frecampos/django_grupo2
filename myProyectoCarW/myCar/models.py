from django.db import models

# Create your models here.
class SliderIndex(models.Model):
    ident = models.CharField(max_length=15,primary_key=True)
    imagen = models.ImageField(upload_to='car',null=True)

    def __str__(self):
        return self.ident

class MisionVision(models.Model):
    ident = models.CharField(max_length=15,primary_key=True)
    mision = models.TextField()
    vision = models.TextField()

    def __str__(self):
        return self.ident

class SliderGaleria(models.Model):
    ident = models.CharField(max_length=15,primary_key=True)
    imagen = models.ImageField(upload_to='car',null=True)
    texto = models.CharField(max_length=65)
    
    def __str__(self):
        return self.ident