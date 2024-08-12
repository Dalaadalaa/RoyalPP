from django.shortcuts import render
from perfumes.models import Perfume 



def home(request):

    perfumes = Perfume.objects.all()
    perfume_list = Perfume.objects.all()
   
    



    context = {
        'perfumes' : perfumes ,
        'perfume_list' : perfume_list ,
        
        
    }

    return render(request , 'index.html' , context)