from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100, verbose_name='Film Adı')
    description = models.TextField(verbose_name='Açıklama')
    image = models.CharField(max_length=100, verbose_name='Film Afişi')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')
    isPublished = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_image_path(self):
        return '/img/' + self.image