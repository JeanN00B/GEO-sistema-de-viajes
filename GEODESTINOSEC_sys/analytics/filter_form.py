from clients.models import Client, Visa, Passport
from sysuserprofile.models import UserProfile
import django_filters as df
import cities_light
import static.metadata_dictionaries as md
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, ButtonHolder, Column, Row, Field, Div, Submit, Button

  


class ClientFilter(df.FilterSet):
    class Meta:
        model = Client
        fields = [
            'id_type', 'client_type',
            'gender', 'civil_status',
            'salesman_refer', 'res_city',
            'res_region', 'res_country',
            # OJO de res_city, filtramos por país y provincia!
            'person_type', 'date_of_birth',
            'budget_capacity', 'academic_level',
            'work_type', 'work_industry',
            'visa__visa_type', 'visa__visa_expire_date',
            'visa__visa_to_country', 'passport__passport_type',
            'passport__passport_expire_date', 'passport__passport_issue_country',
            ]


    id_type = df.MultipleChoiceFilter(
        field_name='id_type', label='Tipo de Identificación', 
        choices=md.ID_TYPE_CHOICES, distinct=True)
    
    client_type = df.ChoiceFilter(
        field_name='client_type', label='Tipo de Cliente',
        choices=md.CLIENT_TYPE_CHOICES)
    
    gender = df.ChoiceFilter(
        field_name='gender', label='Género',
        choices=md.GENDER_CHOICES)
    
    civil_status = df.MultipleChoiceFilter(
        field_name='civil_status', label='Estado civil',
        choices=md.CIVIL_STATUS_CHOICES)
    
    salesman_refer = df.ModelChoiceFilter(
        field_name='salesman_refer', #lable='Vendedor Referente',
        queryset=UserProfile.objects.all())
    
    # If a country is selected -> can select province -> can select city.
    res_country = df.ModelChoiceFilter(
        field_name='res_country', 
        label='País de Residencia',
        queryset=cities_light.models.Country.objects.all())
    
    res_region = df.ModelChoiceFilter(
        field_name='res_region', 
        label='Provincia de Residencia',
        queryset=cities_light.models.Region.objects.all())
    
    res_city = df.ModelChoiceFilter(
        field_name='res_city', 
        label='Ciudad de Residencia',
        queryset=cities_light.models.City.objects.all())

    person_type = df.ChoiceFilter(
        field_name='person_type', label='Tipo de Persona',
        choices=md.PERSON_TYPE_CHOICES)
    
    budget_capacity = df.ChoiceFilter(
        field_name='budget_capacity', label='Nivel de Gasto',
        choices=md.BUDGET_CAPACITY_CHOICES)
    
    academic_level = df.ChoiceFilter(
        field_name='academic_level', label='Nivel Académico',
        choices=md.ACADEMIC_LEVEL_CHOICES)
    
    work_type = df.ChoiceFilter(
        field_name='work_type', label='Tipo de Trabajo',
        choices=md.WORK_TYPE_CHOICES)
    
    work_industry = df.ChoiceFilter(
        field_name='work_industry', label='Sector Ocupacional',
        choices=md.WORK_INDUSTRY_CHOICES)
        
    date_of_birth__range = df.DateFromToRangeFilter(
        field_name='date_of_birth', label='Fecha de Nacimiento',
        lookup_expr='range', widget=df.widgets.RangeWidget)

    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super().__init__(data, queryset, request=request, prefix=prefix)
        self.helper = FormHelper()
        self.helper.form_method = 'GET'
        self.helper.add_input(
            Submit('submit', 'Filtrar', 
                css_class='w-1/4 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded items-center justify-center'),
            )
        self.helper.layout = Layout(
            Field(
                Row(
                    Column(
                        Field('id_type'),
                        Field('client_type'),
                        Field('gender'),
                        Field('civil_status'),
                        Field('salesman_refer'),
                        css_class='bg-gray-200 p-4 rounded-lg w-1/4',
                    ),
                    Column(
                        Field('person_type'),
                        Field('budget_capacity'),
                        Field('academic_level'),
                        Field('work_type'),
                        Field('work_industry'),
                        css_class='bg-gray-200 p-4 rounded-lg w-1/4',
                    ),
                    Column(
                        Column(
                            Field('res_country'),
                            Field('res_region'),
                            Field('res_city'),
                            # TODO append the additional location fields
                        ),
                        Column(
                            Field('visa__visa_type'),
                            Field('visa__visa_to_country'),
                            Field('passport__passport_type'),
                            Field('passport__passport_issue_country'),
                        ),
                        css_class='bg-gray-200 p-4 rounded-lg w-1/4',
                    ),
                    Column(
                        Column(
                            Field('date_of_birth__range'),
                            Field('visa__visa_expire_date'),
                            Field('passport__passport_expire_date'),
                        ),
                        css_class='bg-gray-200 p-4 rounded-lg w-1/4',
                    ),
                ),
            ),
        )


