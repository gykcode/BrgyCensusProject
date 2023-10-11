from django.db import models
from django.utils.safestring import mark_safe

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
MONTHLY_RENTAL = [
            ('1', '1. PhP 500 or less'),
            ('2', '2. PhP 501 - 1,000'),
            ('3', '3. PhP 1,001 - 1,500'),
            ('4', '4. PhP 1,501 - 2,000'),
            ('5', '5. PhP 2,501 - 4,000'),
            ('6', '6. PhP 4,001 - 6,000'),
            ('7', '7. PhP 6,001 - 7,500'),
            ('8', '8. PhP 7,501 - 10,000'),
            ('9', '9. PhP 10,001 and over'),
        ]
CONVENIENCES_CHOICES = [
            ('1', 'a. Refrigerator/ freezer'),
            ('2', 'b. Stove with oven/ gas range'),
            ('3', 'c. Microwave oven'),
            ('4', 'd. Washing Machine'),
            ('5', 'e. Air Conditioner'),
            ('6', 'f. Electric fan and other cooling equipment'),
        ]
ICT_DEVICES_CHOICES = [
            ('1', 'g. Radio/ radio cassete (AM, PM, and transistor)'),
            ('2', 'h. Television'),
            ('3', 'i. CD/ DVD/ VCD'),
            ('4', 'j. Audio component/ stereo set/ karaoke/ videoke'),
            ('5', 'k. Landline/ wireless telephone'),
            ('6', 'l. Mobile phone'),
            ('7', 'm. Tablet'),
            ('8', 'n. Personal computer (desktop, laptop, notebook, netbook, and others)'),
        ]
VEHICLES_CHOICES = [
            ('1', 'o. Car/ van/ jeep/ truck'),
            ('2', 'p. Motorcycle/ motor scooter/ tricycle'),
            ('3', 'q. Bicycle/ pedicap'),
            ('4', 'r. Motorized boat/ banca'),
            ('5', 's. Nonmotorized boat/ banca'),
        ]
INTERNET_ACCESS_CHOICES = [
            ('1', mark_safe('a. fixed (wired) narrowband/ broadband network [e.g. via Digital Subscriber Line (DSL), cable modem, high speed leased line,<br> fiber-to-the-home/building, powerline/ and other fixed (wired) broadband]')),
            ('2', 'b. fixed (wireless) broadband network [e.g. via WiMAX and fixed Code Division Multiple Access (CDMA)]'),
            ('3', 'c. Satelite broadband network'),
            ('4', 'd. Mobile broadband network [e.g. via handset, card (e.g. integrated Subscriber Identify Module or SIM card) or USB modem]'),
        ]
INTERNET_USE_CHOICES = [
            ('1', 'a. Home'),
            ('2', 'b. Work'),
            ('3', 'c. School'),
            ('4', 'd. Another person\'s home'),
            ('5', 'e. Public place'),
            ('6', 'f. Private establishment'),
            ('7', 'g. Internet cafe/ computer shop'),
            ('8', 'h. In mobility'),
        ]
class CensusNewFormModel(models.Model):
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
    birth_registered_1 = models.CharField(max_length=4, null=True, choices=CLOSED_CHOICES, blank=True, default='')
    copy_birthcert_1 = models.CharField(max_length=4, null=True, choices=CLOSED_CHOICES, blank=True, default='')
    marital_status_1 = models.CharField(max_length=4, null=True, choices=MARITAL_STATUS_CHOICES, default='1')

    not_yet_listed = models.CharField(max_length=4, null=True, choices=PERSON_NOT_YET_LISTED_CHOICES, blank=True, default='')
    additional_booklet = models.CharField(max_length=4, null=True, choices=ADDITIONAL_BOOKLET_CHOICES, blank=True, default='')


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

    #3G
    loans_relatives = models.CharField(max_length=4, null=True, choices=CLOSED_CHOICES, blank=True, default='')
    gov_assistance = models.CharField(max_length=4, null=True, choices=CLOSED_CHOICES, blank=True, default='')
    private_bank = models.CharField(max_length=4, null=True, choices=CLOSED_CHOICES, blank=True, default='')
    employer_assistance = models.CharField(max_length=4, null=True, choices=CLOSED_CHOICES, blank=True, default='')
    private_person = models.CharField(max_length=4, null=True, choices=CLOSED_CHOICES, blank=True, default='')
    h3_other = models.CharField(max_length=200, null=True, blank=True)
    monthly_rental_house = models.CharField(max_length=4, null=True, choices=MONTHLY_RENTAL, default='')
    other_residential = models.CharField(max_length=4, null=True, choices=CLOSED_CHOICES, blank=True, default='')
    agricultural_land = models.CharField(max_length=4, null=True, choices=CLOSED_CHOICES, blank=True, default='')
    agricultural_land_reform = models.CharField(max_length=4, null=True, choices=CLOSED_CHOICES, blank=True, default='')
    h11_other = models.CharField(max_length=200, null=True, blank=True)

    #3H
    crop_farm = models.CharField(max_length=4, null=True, choices=CLOSED_CHOICES, blank=True, default='')
    poultry_farm = models.CharField(max_length=4, null=True, choices=CLOSED_CHOICES, blank=True, default='')
    aquafarm = models.CharField(max_length=4, null=True, choices=CLOSED_CHOICES, blank=True, default='')
    fishing_activity = models.CharField(max_length=4, null=True, choices=CLOSED_CHOICES, blank=True, default='')
    h12_other = models.CharField(max_length=200, null=True, blank=True)
    language_specify = models.CharField(max_length=200, null=True, blank=True)
    h14_province = models.CharField(max_length=200, null=True, blank=True)
    h14_municipality = models.CharField(max_length=200, null=True, blank=True)
    conveniences = models.CharField(max_length=200, null=True, blank=True)
    ict_devices = models.CharField(max_length=200, null=True, blank=True)
    vehicles = models.CharField(max_length=200, null=True, blank=True)
    internet_access = models.CharField(max_length=200, null=True, choices=INTERNET_ACCESS_CHOICES, default='')
    internet_use = models.CharField(max_length=200, null=True, blank=True)