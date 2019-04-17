from django.shortcuts import render, get_object_or_404
from models import Craft, Work

def index(request):
    #pull all crafts objects
    Crafts = Craft.objects.all()
    context = {'Craft': Craft,}
    return render(request, 'artist/index.html', {'Crafts':Crafts})
    
#http 404 error
def detail(request, craftid):
    craft = get_object_or_404(Craft, pk=craftid)
    return render(request, 'artist/detail.html', {'craft': craft})

def favorite(request, craftid):
    craft = get_object_or_404(Craft, pk=craftid)
    try:
        select_work = craft.work_set.get(pk=request.POST['work_title'])
        except (KeyError, Work.DoesNotExist):
            return render(request,'artist/detail.html',{
                'craft':craft,
                'error_message': "You did not select a valid Art Work",
            })
        else:
            select_work.is_favorite =True
            select_work.save()
            return render(request, 'music/detail.html', {'craft': craft})