from django.db import models
from django.contrib import admin

# Create your models here.
class Participant(models.Model):
    username = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    institution= models.CharField(max_length=100)

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone', 'email', 'institution')
