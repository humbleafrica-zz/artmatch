from django.contrib import admin
from .models import Craft, Work, Artist, Member, ArtGroup
# Register your models here.

admin.site.register(Craft)
admin.site.register(Work)
admin.site.register(Artist)
admin.site.register(Member)
admin.site.register(ArtGroup)
