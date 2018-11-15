from django.shortcuts import render
from collection.models import Meme

# Create your views here.
def index(request):
    # this is your new view
    memes = Meme.objects.all()
    return render(request, 'index.html', { 'memes': memes,})