from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(max_length=1500, null=False, blank=False)
    rating = models.CharField(max_length=20, null=False, blank=False)
    
