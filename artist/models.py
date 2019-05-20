from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.urlresolvers import reverse

"""Artist"""
class Artist(models.Model):
    #craft choices
    par= "Painting"
    mus= "Music"
    drp= "Performance"
    ptr= "Poet/RAP"
    pho= "Photography" 
    ani= "Animation"
    des= "Design & Architecture"
    cpr= "Computer"
    cer= "Ceramics"
    cal= "Calligraphy"
    asg= "Assemblage"
    drw= "Drawing"
    gri= "Graffiti"
    gra= "Graphic"
    ill= "Illustration"
    mos= "Mosaic"
    scu= "Sculpture"
    vgr= "Videographer"
    
    CRAFT_TYPE_CHOICES=(
        (par, "Painting"),
        (mus, "Music"),
        (drp, "Performance"),
        (ptr, "Poetry"),
        (pho, "Photography"), 
        (ani, "Animation"),
        (des, "Design & Architecture"),
        (cpr, "Computer"),
        (cer, "Ceramics"),
        (cal, "Calligraphy"),
        (asg, "Assemblage"),
        (drw, "Drawing"),
        (gri, "Graffiti"),
        (gra, "Graphic"),
        (ill, "Illustration"),
        (mos, "Mosaic"),
        (scu, "Sculpture"),
        (vgr, "Videographer"),
    )
    
    fname = models.CharField(max_length=50)
    sname = models.CharField(max_length=50)
    stagename = models.CharField(max_length=50)
    craft = models.CharField("Craft", max_length = 20, choices = CRAFT_TYPE_CHOICES)
    speciality = models.CharField(max_length=30, blank=True)
    

    #def voice_concern(self):
    #    self.voted = True,
    #    self.voted = False
        
    def __unicode__(self):
        self.save()
        return self.stagename
    
    class Meta:
        verbose_name = "artist"
        verbose_name_plural = "artists"
        
    
"""Art Catalogue/ Albums"""
class Catalogue(models.Model):
    title = models.CharField(max_length=50)
    year = models.DateField(blank=True, null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    cover_Image = models.ImageField(upload_to='images/')
    
    def __unicode__(self):
        return self.title
        
class Meta:
        verbose_name = "catalogue"
        verbose_name_plural = "catalogues"
    #Album = models.FileField(upload_to='uploads/album')
    
"""ArtForm i.e painting, song , beat, """
class ArtForm(models.Model):
    title = models.CharField(max_length=25)
    genre = models.CharField(max_length=10)
    year = models.DateField(blank=True, null=True)
    cover_Image = models.ImageField(upload_to='images/')
    file = models.FileField(upload_to='artForm/')
    catalogue = models.ForeignKey(Catalogue, on_delete=models.CASCADE)
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = "Art Form"
        verbose_name_plural = "Art Forms"

    
"""Bugs"""
class Bug(models.Model):
    What = models.CharField(max_length=2500)
    Who = models.ForeignKey('Artist', on_delete=models.CASCADE)
    When = models.DateField(blank=True, null=True)
    How = models.CharField(max_length=2500)
    
    def __unicode__(self):
        return self.What
    
    class Meta:
        verbose_name = "bug"
        verbose_name_plural = "bugs"""
    
"""Features"""
class Feature(models.Model):
    What = models.CharField(max_length=2500)
    Who = models.ForeignKey('Artist', on_delete=models.CASCADE)
    When = models.DateField(blank=True, null=True)
    How = models.CharField(max_length=2500)
    
    def __unicode__(self):
        return self.What
    
    class Meta:
        verbose_name = "feature"
        verbose_name_plural = "features"""