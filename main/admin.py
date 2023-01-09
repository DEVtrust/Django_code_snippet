from django.contrib import admin
from .models import Room1
# Register your models here.
from .models import  User

admin.site.register(User)
admin.site.register(Room1)
# admin.site.register(Room1)