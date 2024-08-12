from django.contrib import admin

from .models import Perfume 


class PerfumeAdmin( admin.ModelAdmin):  # instead of ModelAdmin
    
    list_display = ['name' ,'content']
    search_fields = ['name', 'content' ]
   

admin.site.register(Perfume , PerfumeAdmin)

