from django.db import models

# Create your models here.

class CensusFormModel(models.Model):
    enumeration_area_number = models.CharField(max_length=200, null=False, blank=False)
    building_serial = models.CharField(max_length=200, null=False, blank=False)
    housing_unit_serial_number = models.CharField(max_length=200, null=False, blank=False)
    line_number_respondents = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    first_name = models.CharField(max_length=200, null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)

    def Household(self):
        HeadName = '' .join([self.first_name, self.last_name])
        return HeadName
    
