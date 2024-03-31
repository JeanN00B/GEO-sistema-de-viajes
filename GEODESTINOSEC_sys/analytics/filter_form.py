from clients.models import Client, Visa, Passport
from sysuserprofile.models import UserProfile
import django_filters
import cities_light
import static.metadata_dictionaries as md
class ClientFilter(django_filters.FilterSet):
    class Meta:
        model = Client
        fields = {
            'id_type': ['exact'],
            'client_type': ['exact'],
            'gender': ['exact'],
            'civil_status': ['exact'],
            'salesman_refer': ['exact'],
            'res_city': ['exact'],
            # OJO de res_city, filtramos por país y provincia!
            'person_type': ['exact'],
            'date_of_birth': ['exact', 'range'],
            'budget_capacity': ['exact'],
            'academic_level': ['exact'],
            'work_type': ['exact'],
            'work_industry': ['exact'],
            #'work_position': ['exact'],
        }
    '''
    # Check if not selecting any filter, then return clients with any id_type
    id_type = django_filters.ChoiceFilter(field_name='id_type', choices=md.ID_TYPE_CHOICES)
    client_type = django_filters.ChoiceFilter(field_name='client_type', choices=md.CLIENT_TYPE_CHOICES)
    gender = django_filters.ChoiceFilter(field_name='gender', choices=md.GENDER_CHOICES)
    civil_status = django_filters.ChoiceFilter(field_name='civil_status', choices=md.CIVIL_STATUS_CHOICES)
    salesman_refer = django_filters.ModelChoiceFilter(field_name='salesman_refer', queryset=UserProfile.objects.all())
    
    # If a country is selected -> can select province -> can select city.
    kwarg_res_country = django_filters.ModelChoiceFilter(field_name='res_country', queryset=cities_light.models.Country.objects.all())
    kwarg_res_region = django_filters.ModelChoiceFilter(field_name='res_region', queryset=cities_light.models.Region.objects.all())
    kwarg_res_city = django_filters.ModelChoiceFilter(field_name='res_city', queryset=cities_light.models.City.objects.all())

    person_type = django_filters.ChoiceFilter(field_name='person_type', choices=md.PERSON_TYPE_CHOICES)
    budget_capacity = django_filters.ChoiceFilter(choices=md.BUDGET_CAPACITY_CHOICES)
    academic_level = django_filters.ChoiceFilter(choices=md.ACADEMIC_LEVEL_CHOICES)
    work_type = django_filters.ChoiceFilter(choices=md.WORK_TYPE_CHOICES)
    work_industry = django_filters.ChoiceFilter(choices=md.WORK_INDUSTRY_CHOICES)
    
    date_of_birth = django_filters.DateFilter()
    date_of_birth__range = django_filters.DateFromToRangeFilter()
    '''