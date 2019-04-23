from django.contrib import admin
from .models import Artist, GroupMember, Catalogue
# Register your models here.

admin.site.register(Artist)
admin.site.register(GroupMember)
admin.site.register(Catalogue)