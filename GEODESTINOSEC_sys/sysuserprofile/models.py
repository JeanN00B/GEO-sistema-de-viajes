from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class UserProfile(models.Model):
    '''
    This class is used to create a user profile
    user <ForeignKey>: User
    date_of_birth <DateField>: Date of birth
    id_number <IntegerField>: 10 digits max integer
    first_name <CharField>: String
    '''
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    id_number = models.IntegerField(null=False, blank=False, validators=[
        RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='nomatch'),])
    first_name = models.CharField(max_length=30, null=False, blank=False)
    second_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    sur_name = models.CharField(max_length=30, null=False, blank=False)
    phone = models.IntegerField(null=False, blank=False, validators=[
        RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='nomatch'),])
    email = models.EmailField(max_length=40, null=False, blank=False)
    roll = models.CharField(max_length=30, null=False, blank=False, default='user')