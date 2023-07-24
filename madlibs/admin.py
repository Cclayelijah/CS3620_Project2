from django.contrib import admin
from .models import Story, Processed

# Register your models here.
admin.site.register(Story)
admin.site.register(Processed)