from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Menu(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True,upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Content(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    TYPE = (
        ('Menu', 'Menu'),
        ('News', 'Haber'),
        ('Notice', 'Duyuru'),
    )
    menu = models.OneToOneField(Menu, on_delete=models.CASCADE,primary_key=True,) #relation with Menu
    user = models.ForeignKey(User, on_delete=models.CASCADE,)  # relation with User
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    detail = models.TextField()
    type = models.CharField(max_length=10, choices=TYPE)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
