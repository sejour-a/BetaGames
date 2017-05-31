from django.db import models
from .console import Console


class Game(models.Model):
    title = models.CharField(max_length=128, default="Titre du jeu")
    description_short = models.CharField(max_length=512, default="Petite description")
    description_full = models.TextField(default="Description avancée")
    icon = models.ImageField(upload_to='game_icon/', null=True, blank=True)

    consoles = models.ManyToManyField(Console, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)