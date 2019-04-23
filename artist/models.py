from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.urlresolvers import reverse

"""Artist"""
class Artist(models.Model):
    FName = models.CharField(max_length=250)
    SName = models.CharField(max_length=250)
    Stagename = models.CharField(max_length=250)
    Band = models.CharField(max_length=250)
    Genre =models.CharField(max_length=250)
    
    def voice_concern(self):
        self.voted = True,
        self.voted = False
        
    def __str__(self):
        return self.Stagename

"""Band"""
class Band(models.Model):
    Stagename = models.CharField(max_length=250)
    Members = models.CharField(max_length=250)
    def voice_concern(self):
        self.voted = True,
        self.voted = False
        
    def __str__(self):
        return self.Stagename
        
"""Art Group"""
class GroupMember(models.Model):
    Stagename = models.ForeignKey("Artist")
    talent = models.CharField(choices=(
            ('pr', "Painter"),
            ('mu', "Musician"),
            ('dp', "Performance"),
            ('pt', "Poet/RAP"),
            ('ph', "Photography"), 
            ('an', "Animation"),
            ('at', "Architecture"),
            ('cr', "Computer"),
            ('ce', "Ceramics"),
            ('ca', "Calligraphy"),
            ('ag', "Assemblage"),
            ('dr', "Drawing"),
            ('gi', "Graffiti"),
            ('gr', "Graphic"),
            ('il', "Illustration"),
            ('mo', "Mosaic"),
            ('sc', "Sculpture"),
            ('vr', "Videographer"),
        ),
        max_length=3
    )
    
"""Art Catalogue/ Albums"""
class Catalogue(models.Model):
    Title = models.CharField(max_length=500)
    Year = models.DateField(blank=True, null=True)
    Stagename = models.ForeignKey("Artist")
    Band = models.CharField(max_length=250)
    Genre =models.CharField(max_length=250)
    #Album = models.FileField(upload_to='uploads/album')
    
"""Songs"""
class Song(models.Model):
    Title = models.CharField(max_length=500)
    Year = models.DateField(blank=True, null=True)
    Stagename = models.ForeignKey("Artist")
    Band = models.ForeignKey("Band")
    Genre =models.CharField(max_length=250)
    #Upload = models.FileField(upload_to='uploads/instru')
    
"""Bugs"""
class Bug(models.Model):
    What = models.CharField(max_length=2500)
    Who = models.ForeignKey("Artist")
    When = models.DateField(blank=True, null=True)
    How = models.CharField(max_length=2500)
    
"""Features"""
class Feature(models.Model):
    What = models.CharField(max_length=2500)
    Who = models.ForeignKey("Artist")
    When = models.DateField(blank=True, null=True)
    How = models.CharField(max_length=2500)