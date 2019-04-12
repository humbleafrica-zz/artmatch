from __future__ import unicode_literals

from django.db import models

# Create your models here.

#type of art work and artist det

class Crafts(models.Model):
    artist = models.CharField(max_length=250)
    artist_type = models.CharField(max_length=250)
    genre =models.CharField(max_length=250)
    work_image = models.CharField(max_length=1000)
    
    #def__str__(self):
        #return self.work_title + ' - ' + self.artist
        
    #name of art work
class Song_MasterPiece(models.Model):
    collections = models.ForeignKey(Crafts, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=50)
    work_title=models.CharField(max_length=250)