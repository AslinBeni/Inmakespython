from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Author
# Create your views here.
def demo(request):
    obj = Place.objects.all()
    obj1 = Author.objects.all()
    return render(request,"index.html",{'result':obj,'output':obj1})





