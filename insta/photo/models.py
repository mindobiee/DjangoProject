from django.db import models


# Create your models here.
class Photo(models.Model):
    text = models.TextField(blank=True)
    img = models.ImageField(upload_to='timeline_photo/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-created']
