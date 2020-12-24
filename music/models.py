from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Album(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,blank=True)
    image=models.FileField(upload_to='',default='Face.jpg')
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name=models.CharField(max_length=100,blank=True)
    image=models.FileField(upload_to='artistimage',default='')
    language=models.CharField(max_length=100,blank=True)
    album=models.ManyToManyField(Album)

    def __str__(self):
        return self.name

class Song(models.Model):
    name=models.CharField(max_length=100,blank=True)
    artist=models.ForeignKey(Artist,on_delete=models.CASCADE)
    genre=models.CharField(max_length=100,blank=True)
    language=models.CharField(max_length=100,blank=True)
    audio_file=models.FileField(upload_to='audio',default='')
    image=models.FileField(upload_to='songimage',default='')
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

