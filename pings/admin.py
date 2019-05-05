from django.contrib import admin

from .models import Company, Guest, Ping

admin.site.register(Company)
admin.site.register(Guest)
admin.site.register(Ping)

# Register your models here.
