from django.db import models
from django.core.validators import RegexValidator
from static.metadata_dictionaries import *
from phonenumber_field.modelfields import PhoneNumberField
import cities_light

class Client(models.Model):
    # nro, primary key, 10 o passport -> validar con algoritmo?
    id_number = models.CharField(max_length=20, primary_key=True, null=False, validators=[
        RegexValidator(regex='(^\d{10}|^[a-zA-Z0-9]*)$', message='Error ID/RUC/Pasaporte no válido!', code='nomatch')])
    
    id_type = models.CharField(max_length=3, null=True, choices=ID_TYPE_CHOICES, default='None')
    
    client_type = models.CharField(max_length=2, null=False, choices=CLIENT_TYPE_CHOICES, default='P')

    first_name = models.CharField(max_length=20, null=False)
    second_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, null=False)
    sur_name = models.CharField(max_length=20, blank=True, null=True)
    # Generate the fullname from the first_name, second_name, last_name, and sur_name

    image = models.ImageField(upload_to='media/clients/', null=True, blank=True, 
                              height_field=300, width_field=300, max_length=100)
    
    gender = models.CharField(max_length=2, null=True, choices=GENDER_CHOICES, blank=True, default=None)
    
    civil_status = models.CharField(max_length=2, null=True, 
                                    blank=True, choices=CIVIL_STATUS_CHOICES, default=None)
    # +593 ++ 9 dígitos -> validate! 13 exactly
    
    phone = PhoneNumberField(null=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    
    # current session user
    salesman_refer = models.ForeignKey('sysuserprofile.UserProfile', on_delete=models.SET_NULL, null=True, blank=True)  
    
    # TODO EXTRACT city.province & city.country from the city_light model
    res_city = models.ForeignKey('cities_light.City', on_delete=models.SET_NULL, null=True, blank=True, default=None)
    address = models.TextField(max_length=100, null=True, blank=True, default=None)
    
    person_type = models.CharField(max_length=4, null=True, blank=True, choices=PERSON_TYPE_CHOICES, default=None)
        
    date_of_birth = models.DateField(null=True, blank=True)
    
    budget_capacity = models.CharField(max_length=2, null=True, blank=True, default=None, choices=BUDGET_CAPACITY_CHOICES)

    academic_level = models.CharField(max_length=2, null=True, blank=True, default=None, choices=ACADEMIC_LEVEL_CHOICES)
    work_type = models.CharField(max_length=2, null=True, blank=True, default=None, choices=WORK_TYPE_CHOICES)
    work_industry = models.CharField(max_length=5, null=True, blank=True, default=None, choices=WORK_INDUSTRY_CHOICES)
    work_position = models.CharField(max_length=50, null=True, blank=True, default=None)
    company_name = models.CharField(max_length=50, null=True, blank=True, default=None)
    additional_info = models.TextField(max_length=100, null=True, blank=True, default=None)
    


    def __str__(self):
        return f'{self.first_name} {self.last_name} --- {self.id_number}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
class Visa(models.Model):
    visa_holder = models.ForeignKey('Client', on_delete=models.CASCADE, null=False, blank=False)
    visa_number = models.CharField(primary_key=True, max_length=20, null=False)
    visa_type = models.CharField(max_length=3, null=False, choices=VISA_TYPE_CHOICES, default='T')
    visa_issue_date = models.DateField(null=False)
    visa_expire_date = models.DateField(null=False)
    visa_to_country = models.ForeignKey('cities_light.Country', on_delete=models.CASCADE, null=False, blank=False)
    
    def __str__(self):
        return f'{self.visa_holder} --- {self.visa_type} {self.visa_number}'
    
class Passport(models.Model):
    passport_holder = models.ForeignKey('Client', on_delete=models.CASCADE, null=False, blank=False)
    passport_number = models.CharField(primary_key=True, max_length=20, null=False)
    passport_type = models.CharField(max_length=3, null=False, choices=PASSPORT_TYPE_CHOICES)
    passport_issue_date = models.DateField(null=False)
    passport_expire_date = models.DateField(null=False)
    passport_issue_country = models.ForeignKey('cities_light.Country', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return f'{self.passport_holder} --- {self.passport_number}'