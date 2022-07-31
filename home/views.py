from django.shortcuts import render
from.models import Artwork

# Create your views here.
def home(request):
    return render(request,'home/home.html')
def about(request):
    return render(request,'home/about.html')
def org(request):
    return render(request,'home/org.html',{'Artwork': Artwork.objects.all()})
def barn(request):
    return render(request,'home/barn.html')

