from django.contrib import admin

# Register your models here.
from aimfit_app import models

admin.site.register(models.Login)
admin.site.register(models.Trainer)