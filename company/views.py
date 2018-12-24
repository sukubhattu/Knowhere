from django.shortcuts import render
from django.http import HttpResponse
#for image we will import database here
from .models import Image


# Create your views here.
def home(request):
	return render(request, 'company/base.html', {})

def image(request):
#making img bhanne variable
    for i in range(1):
        print (i)
    context = {
    'imgs' : Image.objects.all().order_by('image_name')
    }

    return render(request, 'company/base.html', context)
    endfor