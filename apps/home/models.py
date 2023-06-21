from django.db import models

# Create your models here.

class CensusFormModel(models.Model):
    enumeration_area_number = models.CharField(max_length=200, null=True, blank=True)
    building_serial = models.CharField(max_length=200, null=True, blank=True)
    housing_unit_serial_number = models.CharField(max_length=200, null=True, blank=True)
    household_serial_number = models.CharField(max_length=200, null=True, blank=True)
    line_number_respondents = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)

    # def Household(self):
    #     HeadName = '' .join([self.first_name, self.last_name])
    #     return HeadName

    # def __str__(self):
    #     return self.all()


    
    
