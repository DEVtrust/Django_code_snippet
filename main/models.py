from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import UserManager

class User(AbstractUser):

    email = models.EmailField(_('email address'),unique=True)
    username= models.CharField(max_length=225,null=True, blank=True,unique=True)
   

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    class Meta:
        db_table = u'main_user'
# Create your models here.
class Room1(models.Model):
    Email= models.CharField(max_length=225)
    task= models.CharField(max_length=225)
    Description=models.CharField(max_length=225)
    start=models.DateTimeField()
    end=models.DateTimeField()
    room=models.CharField(max_length=225)
    submeet=models.CharField(max_length=225)
    created_at=models.DateTimeField(default=timezone.now)
    upadted_at=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.task 
