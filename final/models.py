from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    
    fisrt_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
    def _str_(self):
        return self.fisrt_name