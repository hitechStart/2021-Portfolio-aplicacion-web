from django.db import models

class Discografia(models.Model):
    # Agregamos verbose_name a cada campo para setear el nombre de la propiedad.
    title = models.CharField(verbose_name='Titulo', max_length=50)
    description = models.TextField(verbose_name='Descripcion')
    image = models.ImageField(verbose_name='Imagen', upload_to='discografia')
   
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

# creamos la clase Meta para establecer metadatos
    class Meta:
        verbose_name = 'aplicacion'
        verbose_name_plural = 'aplicaciones'
        # Le establecemos el orden en que van a aparecer en el admin
        ordering = ['created']
        
    # Definimos el método __str__ para ver el titulo de la instancia y no el hash
        def __str__(self) -> str:
            return self.title    
    