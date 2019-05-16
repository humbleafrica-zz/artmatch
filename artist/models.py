from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.urlresolvers import reverse

"""Artist"""
class Artist(models.Model):
    User = models.ForeignKey(settings.AUTH_USER_MODEL, editable = False, on_delete=models.CASCADE)
    FName = models.CharField(max_length=50)
    SName = models.CharField(max_length=50)
    Stagename = models.CharField(max_length=50)
    Band = models.CharField(max_length=20)
    Genre =models.CharField(max_length=10)
    
    def voice_concern(self):
        self.voted = True,
        self.voted = False
        
    def __str__(self):
        self.save()
        return self.Stagename
    
    class Meta:
        verbose_name = "artist"
        verbose_name_plural = "artists"
        
"""Band"""
class Band(models.Model):
    Stagename = models.CharField(max_length=50)
    Member = models.ForeignKey(Artist, on_delete=models.CASCADE)
    def voice_concern(self):
        self.voted = True,
        self.voted = False
        
    def __str__(self):
        return self.Stagename
    
    class Meta:
        verbose_name = "band"
        verbose_name_plural = "bands"
        
"""Art Group"""
class Craft(models.Model):
    Stagename = models.ForeignKey(Artist, on_delete=models.CASCADE)
    talent = models.CharField(choices=(
            ('par', "Painting"),
            ('mus', "Music"),
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
    
    class Meta:
        verbose_name = "craft"
        verbose_name_plural = "crafts"
    
"""Art Catalogue/ Albums"""
class Catalogue(models.Model):
    Title = models.CharField(max_length=50)
    Year = models.DateField(blank=True, null=True)
    Stagename = models.ForeignKey(Artist)
    Band = models.ForeignKey(Band, on_delete=models.CASCADE)
    Genre = models.CharField(max_length=250)
    cover = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.Genre
        
class Meta:
        verbose_name = "catalogue"
        verbose_name_plural = "catalogues"
    #Album = models.FileField(upload_to='uploads/album')
    
"""Songs"""
class Song(models.Model):
    Title = models.CharField(max_length=50)
    Year = models.DateField(blank=True, null=True)
    Stagename = models.ForeignKey(Artist, on_delete=models.CASCADE)
    Band = models.ForeignKey(Band, on_delete=models.CASCADE)
    Genre =models.CharField(max_length=10)
    cover = models.ImageField(upload_to='images/')
    file = models.FileField(upload_to='songs/')
    catalogue = models.ForeignKey(Catalogue, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Title
    
    class Meta:
        verbose_name = "song"
        verbose_name_plural = "songs"

"""Beats"""
class Beat(models.Model):
    Title = models.CharField(max_length=50)
    Year = models.DateField(blank=True, null=True)
    Stagename = models.ForeignKey(Artist, on_delete=models.CASCADE)
    Genre =models.CharField(max_length=10)
    cover = models.ImageField(upload_to='images/')
    file = models.FileField(upload_to='songs/')
    def __str__(self):
        return self.Title
    
    class Meta:
        verbose_name = "beat"
        verbose_name_plural = "beats"
    #Upload = models.FileField(upload_to='uploads/instru')
    
"""Photos"""
class Photo(models.Model):
    Title = models.CharField(max_length=50)
    Year = models.DateField(blank=True, null=True)
    Stagename = models.ForeignKey(Artist, on_delete=models.CASCADE)
    Genre =models.CharField(max_length=10)
    cover = models.ImageField(upload_to='images/')
    file = models.FileField(upload_to='songs/')
    def __str__(self):
        return self.Title
    
    class Meta:
        verbose_name = "photo"
        verbose_name_plural = "photos"
        
"""Painting"""
class Painting(models.Model):
    Title = models.CharField(max_length=50)
    Year = models.DateField(blank=True, null=True)
    Stagename = models.ForeignKey(Artist, on_delete=models.CASCADE)
    Genre = models.CharField(max_length=10)
    cover = models.ImageField(upload_to='images/')
    file = models.FileField(upload_to='files/')
    def __str__(self):
        return self.Title
    
    class Meta:
        verbose_name = "painting"
        verbose_name_plural = "paintings"
        
"""Painting"""
class Other(models.Model):
    Title = models.CharField(max_length=50)
    Year = models.DateField(blank=True, null=True)
    Stagename = models.ForeignKey(Artist, on_delete=models.CASCADE)
    Genre = models.CharField(max_length=10)
    cover = models.ImageField(upload_to='images/')
    file = models.FileField(upload_to='files/')
    def __str__(self):
        return self.Title
    
    class Meta:
        verbose_name = "other_Art"
        verbose_name_plural = "other_Arts"
    
"""Bugs"""
class Bug(models.Model):
    What = models.CharField(max_length=2500)
    Who = models.ForeignKey(Artist, on_delete=models.CASCADE)
    When = models.DateField(blank=True, null=True)
    How = models.CharField(max_length=2500)
    
    def __str__(self):
        return self.What
    
    class Meta:
        verbose_name = "bug"
        verbose_name_plural = "bugs"
    
"""Features"""
class Feature(models.Model):
    What = models.CharField(max_length=2500)
    Who = models.ForeignKey(Artist, on_delete=models.CASCADE)
    When = models.DateField(blank=True, null=True)
    How = models.CharField(max_length=2500)
    
    def __str__(self):
        return self.What
    
    class Meta:
        verbose_name = "feature"
        verbose_name_plural = "features"