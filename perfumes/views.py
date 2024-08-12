from django.shortcuts import render

from .models import Perfume

# Create your views here.

def perfume_list(request):
    perfume_list = Perfume.objects.all()
    
    context = {
        'perfume_list': perfume_list,
        
        }
    return render(request, 'perfumes/list.html', context)