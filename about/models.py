from django.db import models

class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='aboutus/', null=True)

    class Meta:
        verbose_name = 'about us'
        verbose_name_plural = 'about us'

    def __str__(self) -> str:
        return self.title






