from django.contrib import admin
from .models import FinesList,Players, PlayerFines

# Register your models here.
admin.site.register(FinesList)
admin.site.register(Players)
admin.site.register(PlayerFines)
