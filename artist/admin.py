from django.contrib import admin
from .models import Artist, Catalogue, ArtForm

admin.site.register(Artist)
admin.site.register(Catalogue)
#admin.site.register(Bug)
#admin.site.register(Feature)
admin.site.register(ArtForm)

#admin.site.register(Catalogue)