from django.db import models
from django.contrib import messages
from django.core.validators import RegexValidator
from static.metadata_dictionaries import *
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    # nro, primary key, 10 o passport -> validar con algoritmo?
    id_number = models.CharField(max_length=20, primary_key=True, null=False, validators=[
        RegexValidator(regex='(^\d{10}|^w*)$', message='Error ID/RUC/Pasaporte no válido!', code='nomatch')])
    
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
    
    province = models.CharField(max_length=20, null=True, blank=True, choices=PROVINCES_CHOICES, default=None)
    
    city = models.CharField(max_length=32, null=True, blank=True, choices=CITIES_CHOICES, default=None)
    
    address = models.TextField(max_length=100, null=True, blank=True, default=None)
    
    person_type = models.CharField(max_length=4, null=True, blank=True, choices=PERSON_TYPE_CHOICES, default=None)
    
    nationality = models.CharField(max_length=20, null=True, blank=True, default=None, choices=NATIONALITIES_CHOICES)
    
    date_of_birth = models.DateField(null=True, blank=True)
    
    budget_capacity = models.CharField(max_length=2, null=True, blank=True, default=None, choices=BUDGET_CAPACITY_CHOICES)

    work_industry = models.CharField(max_length=50, null=True, blank=True, default=None)
    work_position = models.CharField(max_length=50, null=True, blank=True, default=None)
    company_name = models.CharField(max_length=50, null=True, blank=True, default=None)
    additional_info = models.TextField(max_length=100, null=True, blank=True, default=None)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} --- {self.id_number}'

    def save(self, *args, **kwargs):
        # 2. validate city in province
        if self.province != None and self.city != None:
            if self.city not in PROVINCES_CITIES_ECUADOR[self.province]:
                raise ValueError('City has to belong to the selected province')
        else:
            pass
        super().save(*args, **kwargs)