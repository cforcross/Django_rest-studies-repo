from django.contrib import admin

# Register your models here.
from .models import Todo
# Create your views here.
admin.site.register(Todo)
