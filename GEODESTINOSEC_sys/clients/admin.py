from django.contrib import admin
from .models import Client, Visa, Passport

admin.site.register(Client)
admin.site.register(Visa)
admin.site.register(Passport)