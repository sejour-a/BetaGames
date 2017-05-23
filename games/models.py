from django.db import models


class Console(models.Model):
    name = models.CharField(max_length=128, default="Nom de la console")
    description_short = models.CharField(max_length=128, default="Petite description")
    description_full = models.TextField(default="Description avancée")
    icon = models.ImageField(upload_to='console_icon', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


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


class Screenshot(models.Model):
    title = models.CharField(max_length=128, default="")
    description = models.CharField(max_length=512, default="")
    image = models.ImageField(upload_to='screenshots/', null=False, blank=True)

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    support = models.ForeignKey(Console, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
