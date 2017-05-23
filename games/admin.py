from django.contrib import admin

from .models import Game, Screenshot, Console

admin.site.register(Game)
admin.site.register(Screenshot)
admin.site.register(Console)
