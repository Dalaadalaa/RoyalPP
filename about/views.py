from django.shortcuts import render

from .models import AboutUs


def aboutus_list(request):
    about = AboutUs.objects.last()
    

    context = {
        'about' : about ,
        
    }

    return render(request , 'about.html' , context)