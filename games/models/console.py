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
