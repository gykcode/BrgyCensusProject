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
            ('Yes', '1: YES'),
            ('No', '2: NO'),
        ]

MARITAL_STATUS_CHOICES = [
            ('1', 'SINGLE'),
            ('2', 'MARRIED'),
            ('3', 'COMMON LAW/ LIVE-IN'),
            ('4', 'WIDOWED'),
            ('5', 'DIVORCED/ SEPARATED/ ANNULLED'),
        ]
PERSON_NOT_YET_LISTED_CHOICES = [
            ('1', 'Yes, add to the list'),
            ('2', 'None'),
        ]
ADDITIONAL_BOOKLET_CHOICES = [
            ('1', 'Yes, use additional booklet'),
            ('2', 'None'),
        ]
HEALTH_PROBLEM_CHOICES = [
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
        ]
TYPE_OF_BUILDING_CHOICES = [
            ('1', '1. Single house'),
            ('2', '2. Duplex'),
            ('3', '3. Apartment/accesories/ rowhouse'),
            ('4', '4. Condominium/condotel'),
            ('5', '5. Other multi-unit residential'),
            ('6', '6. Commercial/industrial/ agricultural (eg. office, factory, barn)'),
            ('7', '7. Institutional living quarter	(e.g. hotel, hospital, convent, jail)'),
            ('8', '8. Other types of building (e.g. bus/trailer, boat, tent), SPECIFY'),
            ('9', '9. None (e.g. homeless, cart), END INTERVIEW'),
        ]
NUMBER_OF_FLOORS = [
            ('1', '1. One floor (e.g. bungalow, including basement/ mezzanine floor)'),
            ('2', '2. Two floor'),
            ('3', '3. Three floors'),
            ('4', '4. Four floors'),
            ('5', '5. Five to 10 floors'),
            ('6', '6. 11 floors or more'),
        ]
YEAR_BUILT = [
            ('1', '1. 2020'),
            ('2', '2. 2019'),
            ('3', '3. 2018'),
            ('4', '4. 2017'),
            ('5', '5. 2016'),
            ('6', '6. 2011-2015'),
            ('7', '7. 2001-2010'),
            ('8', '8. 1991-2000'),
            ('9', '9. 1981-1990'),
            ('10', '10. 1980 or earlier'),
            ('11', '11. Don\'t know'),
        ]
FLOOR_AREA_HOUSE_UNIT = [
            ('1', '1. Less than 5 sq.m. or Less that 54 sq.ft.'),
            ('2', '2. 5-9 sq.m. or 54-107 sq.ft.'),
            ('3', '3. 10-19 sq.m. or 108-209 sq.ft.'),
            ('4', '4. 20-29 sq.m. or 210-317 sq.ft.'),
            ('5', '5. 30-49 sq.m. or 318-532 sq.ft.'),
            ('6', '6. 50-69 sq.m. or 533-748 sq.ft.'),
            ('7', '7. 70-89 sq.m. or 749-963 sq.ft.'),
            ('8', '8. 90-119 sq.m. or 964-1,286 sq.ft.'),
            ('9', '9. 120-149 sq.m. or 1,287-1609 sq.ft.'),
            ('10', '10. 150-199 sq.m. or 1610-2147 sq.ft.'),
            ('11', '11. 200 sq.m. and over or 2148 sq.ft. and over'),
        ]
TENURE_STATUS = [
            ('1', '1. Own or owner-like possesion of the house and lot'),
            ('2', '2. Own house, rent lot'),
            ('3', '3. Own house, rent-free lot with consent of owner'),
            ('4', '4. Own house, rent-free lot without consent of owner'),
            ('5', '5. Rent house/room, including lot'),
            ('6', '6. Rent-free house and lot with consent of owner'),
            ('7', '7. Rent-free house and lot without consent of owner'),
        ]
ACQUISITION_HOUSE = [
            ('1', '1. Inherited'),
            ('2', '2. Gift'),
            ('3', '3. Company benefit'),
            ('4', '4. Purchased'),
            ('5', '5. Other, Specify'),
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

    not_yet_listed = models.CharField(max_length=4, choices=PERSON_NOT_YET_LISTED_CHOICES, blank=True, default='')
    additional_booklet = models.CharField(max_length=4, choices=ADDITIONAL_BOOKLET_CHOICES, blank=True, default='')


    #3C
    religion_1 = models.CharField(max_length=200, null=True, blank=True)
    citizen_1 = models.CharField(max_length=4, choices=CLOSED_CHOICES, blank=True, default='')
    other_country_1 = models.CharField(max_length=200, null=True, blank=True)
    ethnicity_1 = models.CharField(max_length=200, null=True, blank=True)
    health_problem_a_1 = models.CharField(max_length=4, choices=HEALTH_PROBLEM_CHOICES, blank=True, default='')
    health_problem_b_1 = models.CharField(max_length=4, choices=HEALTH_PROBLEM_CHOICES, blank=True, default='')
    health_problem_c_1 = models.CharField(max_length=4, choices=HEALTH_PROBLEM_CHOICES, blank=True, default='')
    health_problem_d_1 = models.CharField(max_length=4, choices=HEALTH_PROBLEM_CHOICES, blank=True, default='')
    health_problem_e_1 = models.CharField(max_length=4, choices=HEALTH_PROBLEM_CHOICES, blank=True, default='')
    health_problem_f_1 = models.CharField(max_length=4, choices=HEALTH_PROBLEM_CHOICES, blank=True, default='')
    remarks_3C = models.CharField(max_length=200, null=True, blank=True)

    #3D
    province_time_birth_1 = models.CharField(max_length=200, null=True, blank=True)
    municipality_time_birth_1 = models.CharField(max_length=200, null=True, blank=True)
    province_reside_1 = models.CharField(max_length=200, null=True, blank=True)
    municipality_reside_1 = models.CharField(max_length=200, null=True, blank=True)
    read_write_1 = models.CharField(max_length=4, choices=CLOSED_CHOICES, blank=True, default='')
    highest_year_completed_1 = models.CharField(max_length=200, null=True, blank=True)
    attend_school_1 = models.CharField(max_length=4, choices=CLOSED_CHOICES, blank=True, default='')
    province_school_attended_1 = models.CharField(max_length=200, null=True, blank=True)
    municipality_school_attended_1 = models.CharField(max_length=200, null=True, blank=True)
    overseas_worker_1 = models.CharField(max_length=4, choices=CLOSED_CHOICES, blank=True, default='')

    #3E
    usual_activity_1 = models.CharField(max_length=200, null=True, blank=True)
    business_worked_1 = models.CharField(max_length=200, null=True, blank=True)
    kind_of_worker_1 = models.CharField(max_length=200, null=True, blank=True)
    province_work_past12months_1 = models.CharField(max_length=200, null=True, blank=True)
    municipality_work_past12months_1 = models.CharField(max_length=200, null=True, blank=True)
    children_borned_1 = models.IntegerField(null=True, blank=True)
    children_still_living_1 = models.IntegerField(null=True, blank=True)
    children_alive_specificdate_1 = models.IntegerField(null=True, blank=True)
    age_firstmarriage_1 = models.IntegerField(null=True, blank=True)
    remarks_3E = models.CharField(max_length=200, null=True, blank=True)
    
    #3F
    type_of_building = models.CharField(max_length=200, null=True, choices=TYPE_OF_BUILDING_CHOICES, default='')
    type_of_building_specify = models.CharField(max_length=200, null=True, blank=True)
    number_of_floors = models.CharField(max_length=200, null=True, choices=NUMBER_OF_FLOORS, default='')
    year_building_built = models.CharField(max_length=200, null=True, choices=YEAR_BUILT, default='')
    floor_area_of_housing = models.CharField(max_length=200, null=True, choices=FLOOR_AREA_HOUSE_UNIT, default='')
    tenure_status_of_housing = models.CharField(max_length=200, null=True, choices=TENURE_STATUS, default='')
    acquisition_of_housing = models.CharField(max_length=200, null=True, choices=ACQUISITION_HOUSE, default='')
    acquisition_of_housing_specify = models.CharField(max_length=200, null=True, blank=True)