from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

#type of art work and artist det
class Craft(models.Model):
    """A model of craft groupings"""
    artist = models.ForeignKey("Artist")
    craft_title = models.CharField(max_length=500)
    craft_logo = models.CharField(max_length=1000)
    
    def get_absolute_url(self):
        return reverse('artist: detail', kwargs={'pk':self.pk})
    
    def __str__(self):
        return self.craft_title + ' - '+ self.artist
    
#name of art work
class Work(models.Model):
    """A model of artworks"""
    work_id = models.ForeignKey(Craft, on_delete=models.CASCADE)
    work_media = models.CharField(max_length=250)
    work_title = models.CharField(max_length=250)

    def __str__(self):
        return self.work_title
        
class Artist(models.Model):
    """A model of a artist"""
    Artist = models.CharField(max_length=250)
    name = models.CharField(max_length=500)
    crafts =models.TextField(max_length=5000)
    genre =models.CharField(max_length=250)

class ArtGroup(models.Model):
    """A model of a artgroup"""
    name = models.CharField(max_length=200)
    can_paint = models.BooleanField(default=False)
    can_draw = models.BooleanField(default=False)
    can_sing = models.BooleanField(default=False)
    can_rap = models.BooleanField(default=False)
    can_dance = models.BooleanField(default=False)
    can_snap = models.BooleanField(default=False)
    can_perform = models.BooleanField(default=False)
    can_narrate = models.BooleanField(default=False)
    can_playInst = models.BooleanField(default=False)
    can_other = models.BooleanField(default=False)
    artist = models.ForeignKey("Artist")

class Member(models.Model):
    """A model of a art group member."""
    name = models.CharField("Member's name", max_length=200)
    talent = models.CharField(choices=(
            ('pr', "Painter"),
            ('mu', "Musician"),
            ('dp', "Drama/ Performance"),
            ('pt', "poet/RAP"),
            ('pt', "poet/RAP"),
        ),
        max_length=3
    )
    group = models.ForeignKey("ArtGroup")