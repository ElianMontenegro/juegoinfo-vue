from django.db import models

# from .managers import JuegoManager

class Juego(models.Model):
    """Model definition for Juego."""

    name = models.CharField("nombre del juego", max_length=40)

    description = models.TextField(
        'Descripcion de la categoria',
        blank=True,
    )
    price = models.FloatField(default=0)

    image = models.URLField( blank=True)

    link_url = models.URLField( blank=True)

    backimage = models.URLField( blank=True)


    #objects = JuegoManager()

    class Meta:
        verbose_name = 'Juego'
        verbose_name_plural = 'Juegos'

    def __str__(self):
        return str(self.id) + '-' + self.name

