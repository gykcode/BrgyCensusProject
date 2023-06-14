from django.db import models

# Create your models here.
class LastName(models.Model):
    last_name = models.CharField(max_length=200, null=False, blank=False)
    def __str__(self):
        return self.last_name
        
class FirstName(models.Model):
    first_name = models.CharField(max_length=200, null=False, blank=False)
    def __str__(self):
        return self.first_name

