from django.db import models
from django.conf import settings

# Create your models here.


class blogPost(models.Model):
    cover = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=150)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    