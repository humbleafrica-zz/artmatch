from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.urlresolvers import reverse

"""Artist"""
class Artist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, editable = False)
    FName = models.CharField(max_length=250)
    SName = models.CharField(max_length=250)
    Stagename = models.CharField(max_length=250)
    Band = models.CharField(max_length=250)
    Genre =models.CharField(max_length=250)
    
    def voice_concern(self):
        self.voted = True,
        self.voted = False
        
    def __str__(self):
        self.save()
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
class Craft(models.Model):
    Stagename = models.ForeignKey("Artist")
    talent = models.CharField(choices=(
            ('par', "Painter"),
            ('mus', "Musician"),
            ('drp', "Performance"),
            ('ptr', "Poet/RAP"),
            ('pho', "Photography"), 
            ('ani', "Animation"),
            ('ate', "Architecture"),
            ('cpr', "Computer"),
            ('cer', "Ceramics"),
            ('cal', "Calligraphy"),
            ('asg', "Assemblage"),
            ('drw', "Drawing"),
            ('gri', "Graffiti"),
            ('gra', "Graphic"),
            ('ill', "Illustration"),
            ('mos', "Mosaic"),
            ('scu', "Sculpture"),
            ('vgr', "Videographer"),
        ),
        max_length=3
    )
    
    def __str__(self):
        return self.talent
    
"""Art Catalogue/ Albums"""
class Catalogue(models.Model):
    Title = models.CharField(max_length=500)
    Year = models.DateField(blank=True, null=True)
    Stagename = models.ForeignKey("Artist")
    Band = models.CharField(max_length=250)
    Genre = models.CharField(max_length=250)
    cover = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.Genre
    #Album = models.FileField(upload_to='uploads/album')
    
"""Songs"""
class Song(models.Model):
    Title = models.CharField(max_length=500)
    Year = models.DateField(blank=True, null=True)
    Stagename = models.ForeignKey("Artist")
    Band = models.ForeignKey("Band")
    Genre =models.CharField(max_length=250)
    cover = models.ImageField(upload_to='images/')
    file = models.FileField(upload_to='songs/')
    def __str__(self):
        return self.Title
        
class Beat(models.Model):
    Title = models.CharField(max_length=500)
    Year = models.DateField(blank=True, null=True)
    Stagename = models.ForeignKey("Artist")
    Genre =models.CharField(max_length=250)
    cover = models.ImageField(upload_to='images/')
    file = models.FileField(upload_to='songs/')
    def __str__(self):
        return self.Title        
    #Upload = models.FileField(upload_to='uploads/instru')
    
"""Bugs"""
class Bug(models.Model):
    What = models.CharField(max_length=2500)
    Who = models.ForeignKey("Artist")
    When = models.DateField(blank=True, null=True)
    How = models.CharField(max_length=2500)
    def __str__(self):
        return self.What
    
"""Features"""
class Feature(models.Model):
    What = models.CharField(max_length=2500)
    Who = models.ForeignKey("Artist")
    When = models.DateField(blank=True, null=True)
    How = models.CharField(max_length=2500)
    def __str__(self):
        return self.What