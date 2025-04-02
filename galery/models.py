from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Image(models.Model):

    CATEGORIES = [
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('GALÁXIA', 'Galáxia'),
        ('PLANETA', 'Planeta'),
    ]

    name = models.CharField(max_length=100, null=False, blank=False)
    caption = models.CharField(max_length=150, null=False, blank=False)
    category = models.CharField(max_length=100, choices=CATEGORIES, default='')
    description = models.TextField(null=False, blank=False)
    photograph = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    published = models.BooleanField(default=False)
    date_photograph = models.DateTimeField(default=datetime.now, blank=False)
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user'
    )

    def __str__(self):
        return self.name