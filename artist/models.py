from __future__ import unicode_literals
from django.db import models

#type of art work and artist det
class Craft(models.Model):
    craft_artist = models.CharField(max_length=250)
    craft_Title = models.CharField(max_length=500)
    craft_Type = models.CharField(max_length=250)
    genre =models.CharField(max_length=250)
    work_Image = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.craft_title + ' - '+ self.artist
    
#name of art work
class Work(models.Model):
    work = models.ForeignKey(Craft, on_delete=models.CASCADE)
    work_media = models.CharField(max_length=250)
    work_title = models.CharField(max_length=250)

    def __str__(self):
        return self.work_title