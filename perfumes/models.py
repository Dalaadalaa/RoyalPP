    
from django.db import models
from django.utils.text import slugify

# Create your models here.

class Perfume(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
   
    
    image = models.ImageField(upload_to='perfumes/')
    slug = models.SlugField(blank=True, null=True)


    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Perfume, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'perfume'
        verbose_name_plural = 'perfumes'

    def __str__(self) -> str:
        return self.name

  
