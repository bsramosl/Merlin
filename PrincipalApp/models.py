from django.db import models
 

class Categoria(models.Model):
    nombre = models.CharField(max_length=50,blank=False,null=False)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nombre']

    def __srt__(self):
        return self.nombre


class Pregunta (models.Model):
    descripcion = models.CharField(max_length=250,blank=False,null=False)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    a = models.CharField(max_length=20,blank=False,null=False)
    b = models.CharField(max_length=20,blank=False,null=False)
    c = models.CharField(max_length=20,blank=False,null=False)
    d = models.CharField(max_length=20,blank=False,null=False)

    class Meta:
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'
        ordering = ['descripcion']

    def __srt__(self):
        return self.descripcion
        