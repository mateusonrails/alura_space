from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    caption = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    photograph = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return f'Image [name={self.name}]'