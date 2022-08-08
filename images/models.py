from django.db import models
from django.conf import settings
from autoslug import AutoSlugField

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    url = models.URLField()
    slug = AutoSlugField(unique=True, populate_from='title')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True, db_index=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created', on_delete=models.CASCADE)

    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)

    def __str__(self):
        return self.title
    
