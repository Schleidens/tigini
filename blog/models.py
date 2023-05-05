from django.db import models
from django.conf import settings
from PIL import Image
from io import BytesIO
from django.core.files import File

# Create your models here.


class blogPost(models.Model):
    cover = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=150)
    slug = models.SlugField(default="", unique=True, null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
    def save(self, *args, **kwargs):
        if self.cover:
            # Open the image using Pillow
            image = Image.open(self.cover)
            
            #check the image size before resize and Compress
            width, height = image.size
            if width > 1024 or height > 1024:
                max_size = (1024, 1024)
                
            #Resize the image to a maximum size of 1024 x 1024 pixels
            image.thumbnail(max_size)
            
            # Compress the image
            if self.cover.name.lower().endswith('.jpg') or self.cover.name.lower().endswith('.jpeg'):
                format = 'JPEG'
                # Set the JPEG quality level to 80%
            elif self.cover.name.lower().endswith('.png'):
                format = 'PNG'
                # Set the PNG compression level to 6 (out of 9)
                image = image.convert('P', palette=Image.ADAPTIVE, colors=256)
                options = {'compress_level': 6}
            else:
                # Unsupported image format
                super(blogPost, self).save(*args, **kwargs)
                return
            
            output = BytesIO()
            image.save(output, format=format, optimize=True, quality=80, **options if format == 'PNG' else {})
            new_image = File(output, name=self.cover.name)

            # Set the image field to the compressed image
            self.cover = new_image

        super(blogPost, self).save(*args, **kwargs)