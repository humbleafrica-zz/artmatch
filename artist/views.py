from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Craft, Work, Artist, ArtGroup, Member

class IndexView(generic.ListView):
    templateName = 'artist/index.html'
    
    def get_queryset(self):
        return Craft.objects.all()

class DetailView(generic.DetailView):
    model=Craft
    templateName = 'artist/detail.html'
    
class ArtistCreate(CreateView):
    model = Artist
    fields =['artist', 'craft_title', 'genre', 'craft_logo']