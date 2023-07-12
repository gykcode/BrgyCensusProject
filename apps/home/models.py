from django.db import models

# Create your models here.
MODE_CHOICES = [
            ('PAPI', 'PAPI'),
            ('SAQ', 'SAQ'),
            ('CAPI', 'CAPI'),
        ]
RESULT_CHOICES = [
            ('1', '1. COMPLETED'),
            ('2', '2. NOT YET COMPLETED (FOR CALLBACK)'),
            ('3', '3. ENTRIRE HOUSEHOLD IS ABSENT/AWAY DURING THE ENUMERATION PERIOD'),
            ('4', '4. REFUSED'),
            ('5', '5. OTHERS, SPECIFY'),
        ]

RELATIONSHIP_CHOICES = [
            ('1', 'Head'),
            ('2', 'Spouse of the head'),
            ('3', 'Never-married children of the head/spouse, from the oldest to the youngest'),
            ('4', 'Ever-married children of the head/spouse, from the oldest to the youngest'),
            ('5', 'Other relatives of the head'),
            ('6', 'Nonrelatives of the head'),
        ]

GENDER_CHOICES = [
            ('1', 'MALE'),
            ('2', 'FEMALE'),
        ]

CLOSED_CHOICES = [
            ('1', 'YES'),
            ('2', 'NO'),
        ]

MARITAL_STATUS_CHOICES = [
            ('1', 'SINGLE'),
            ('2', 'MARRIED'),
            ('3', 'COMMON LAW/ LIVE-IN'),
            ('4', 'WIDOWED'),
            ('5', 'DIVORCED/ SEPARATED/ ANNULLED'),
        ]

class CensusFormModel(models.Model):
    #3A
    enumeration_area_number = models.CharField(max_length=200, null=True, blank=True)
    building_serial = models.CharField(max_length=200, null=True, blank=True)
    housing_unit_serial_number = models.CharField(max_length=200, null=True, blank=True)
    household_serial_number = models.CharField(max_length=200, null=True, blank=True)
    line_number_respondents = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)

    # visit number
    date_time_created_1 = models.DateTimeField( null=True, blank=True )
    date_time_ended_1 = models.DateTimeField( null=True, blank=True )
    result_1 = models.CharField(max_length=4, choices=RESULT_CHOICES, blank=True, default='')
    result_description_1 = models.IntegerField( null=True, blank=True )

    date_time_created_2 = models.DateTimeField( null=True, blank=True )
    date_time_ended_2 = models.DateTimeField( null=True, blank=True )
    result_2 = models.CharField(max_length=4, choices=RESULT_CHOICES, blank=True, default='')
    result_description_2 = models.IntegerField( null=True, blank=True )

    date_time_created_3 = models.DateTimeField( null=True, blank=True )
    date_time_ended_3 = models.DateTimeField( null=True, blank=True )
    result_3 = models.CharField(max_length=4, choices=RESULT_CHOICES, blank=True, default='')
    result_description_3 = models.IntegerField( null=True, blank=True )
    

    #appointment for the next visit
    appointment_date_time_1 = models.DateTimeField( null=True, blank=True )
    appointment_date_time_2 = models.DateTimeField( null=True, blank=True )
    appointment_date_time_3 = models.DateTimeField( null=True, blank=True )



    #summary of visit
    number_of_visit = models.IntegerField(null=True, blank=True)
    result_of_final_visit = models.IntegerField(null=True, blank=True)
    number_of_household_member = models.IntegerField(null=True, blank=True)
    number_male = models.IntegerField(null=True, blank=True)
    number_female = models.IntegerField(null=True, blank=True)
    enumerator_code = models.IntegerField(null=True, blank=True)
    mode_of_data_collection = models.CharField(max_length=4, choices=MODE_CHOICES, default='PAPI')


    #3B
    residing_fullname_1 = models.CharField(max_length=200, null=True, blank=True)
    relationship_to_head_1 = models.CharField(max_length=4, choices=RELATIONSHIP_CHOICES, blank=True, default='')
    gender_1 = models.CharField(max_length=4, choices=GENDER_CHOICES, blank=True, default='')
    date_born_1 = models.DateTimeField( null=True, blank=True )
    age_1 = models.IntegerField(null=True, blank=True)
    birth_registered_1 = models.CharField(max_length=4, choices=CLOSED_CHOICES, blank=True, default='')
    copy_birthcert_1 = models.CharField(max_length=4, choices=CLOSED_CHOICES, blank=True, default='')
    marital_status_1 = models.CharField(max_length=4, choices=MARITAL_STATUS_CHOICES, default='1')
   
    
