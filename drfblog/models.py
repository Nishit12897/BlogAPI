from django.conf import settings
from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


# Create your models here.

class Blog(models.Model):
    # pk aka id --> numbers
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    category = models.CharField(max_length=120, null=True, blank=True)
    date = models.DateTimeField(max_length=120, null=True, blank=True)
    blogimg = models.ImageField(upload_to='blog_img')
    status = models.CharField(max_length=120, null=True, blank=True)
