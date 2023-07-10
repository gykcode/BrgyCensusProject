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

    # visit number
    date_1 = models.DateTimeField(null=True, blank=True)
    time_begin_1 = models.DateTimeField(null=True, blank=True)
    time_ended_1 = models.DateTimeField(null=True, blank=True)  
    # result_1 = 

    #appointment for the next visit

    #summary of visit
    number_of_visit = models.IntegerField(null=True, blank=True)
    result_of_final_visit = models.IntegerField(null=True, blank=True)
    number_of_household_member = models.IntegerField(null=True, blank=True)
    number_male = models.IntegerField(null=True, blank=True)
    number_female = models.IntegerField(null=True, blank=True)
    enumerator_code = models.IntegerField(null=True, blank=True)
    mode_of_data_collection = models.CharField(max_length=4, null=True, blank=True)

    def firstdate(self):
        return self.date_1.strftime('%B %d')

# class InterviewRecordModel(models.Model):
   
    
