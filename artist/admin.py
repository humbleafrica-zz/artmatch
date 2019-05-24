from django.contrib import admin
from .models import Artist, Catalogue, Bug, Feature, ArtForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.register(Artist)
admin.site.register(Catalogue)
admin.site.register(Bug)
admin.site.register(Feature)
admin.site.register(ArtForm)

#admin.site.register(Catalogue)

class ArtistInline(admin.StackedInline):
    model = Artist
    can_delete = False
    verbose_name_plural = 'Artist'
    fk_name = 'stagename'

class CustomUserAdmin(UserAdmin):
    inlines = (ArtistInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)