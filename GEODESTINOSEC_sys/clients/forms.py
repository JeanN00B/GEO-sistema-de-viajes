from django import forms
from .models import Client, Visa, Passport
from django_select2 import forms as s2forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
import cities_light
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, ButtonHolder, Column, Row, Field, Div, Submit, Button
from static.metadata_dictionaries import *
#from image_uploader_widget.widgets import ImageUploaderWidget
from sysuserprofile.models import UserProfile
from django.core.cache import cache


'''
Don't include the ID type, and the salesman_refer, those
values are getting obtained by default
''' 
class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ['salesman_refer']
        labels = {
            'id_number': 'Número de Identificación',
            #'id_type': 'Tipo de Identificación',
            'client_type': 'Tipo de Cliente',
            'first_name': 'Primer Nombre',
            'image': 'Foto del cliente',
            'second_name': 'Segundo Nombre',
            'last_name': 'Primer Apellido',
            'sur_name': 'Segundo Apellido',
            'gender': 'Género',
            'civil_status': 'Estado Civil',
            'phone': 'Teléfono celular',
            'email': 'Correo electrónico',
            'res_city': 'Ciudad / Provincia / País',
            'academic_level': 'Nivel Académico',
            'address': 'Dirección',
            'person_type': 'Tipo de Persona',
            'nationality': 'Nacionalidad',
            'date_of_birth': 'Fecha de Nacimiento',
            'budget_capacity': 'Nivel de gasto',
            'work_industry': 'Sector ocupacional',
            'work_position': 'Cargo de Trabajo',
            'company_name': 'Nombre de la Empresa',
            'additional_info': 'Información Adicional',
            'work_type': 'Tipo de Trabajo',
        }

    date_of_birth = forms.DateField(
        label='Fecha de Nacimiento',
        widget=forms.SelectDateWidget(attrs={
            'style': 'width: 32%; margin-left: 0.25rem; background-color: white; border-radius: 0.5rem; border: 1px solid #D1D5DB; padding-top: 0.5rem; padding-bottom: 0.5rem; padding-left: 0.2rem; padding-right: 0.2rem;',},
            years=range(1880, 2030),
            empty_label=("Año", "Mes", "Día"),
            ),
        required=False,
    )

    gender = forms.ChoiceField(
        label='Género',
        widget=forms.RadioSelect(),
        choices=GENDER_CHOICES,
        required=False,
    )

    id_type = forms.ChoiceField(
        choices=ID_TYPE_CHOICES,
        widget = forms.HiddenInput(
            attrs={'value': 'PP', 'style': 'display: none'},
        ),
    )

    person_type = forms.ChoiceField(
        label='Tipo de Persona',
        choices=PERSON_TYPE_CHOICES,
        widget=forms.RadioSelect(),
        required=False,
    )

    address = forms.Field(
        label='Dirección',
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False,
    )

    additional_info = forms.Field(
        label='Información Adicional',
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False,
    )

    client_type = forms.ChoiceField(
        label='Tipo de Cliente',
        choices=CLIENT_TYPE_CHOICES,
        initial='P',
        widget=forms.RadioSelect(),
        required=False,
    )

    phone = PhoneNumberField(
        label='Teléfono celular',
        widget=PhoneNumberPrefixWidget(
            number_attrs={'class': 'ml-1 form-control bg-white rounded-lg border border-gray-300 py-2 px-4',
                          'style': 'width: 53%;'},
            country_attrs={'class': 'mr-1 form-control bg-white rounded-lg border border-gray-300 py-2 px-2',
                            'style': 'width: 44%;'},
            initial='EC',
            )
        )

    """
    res_city = forms.ModelChoiceField(
        label='Ciudad / Provincia / País',
        queryset=cities_light.models.City.objects.all(),
        widget=s2forms.Select2Widget(),
        required=False,
        )
    """
    res_city = s2forms.ModelSelect2Widget(
        queryset=cache.get_or_set('cached_cities', cities_light.models.City.objects.all(), 60*60*2)
    )
        
    image = forms.ImageField(
        label='Foto del cliente',
        required= False,
    )

    def __init__(self, *args, **kwargs):
        super(AddClientForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field(
                Row(
                    Column(
                        HTML('<h2 class="my-2 py-1 text-xl font-bold text-white bg-blue-400 rounded-lg text-center">Datos principales</h2>'),
                        'id_number', 'id_type', 'first_name', 'second_name', 'last_name', 
                        'sur_name', 'phone', 'email', 'client_type',
                        style="margin-bottom: 5px; border: 2px solid #a4a5a5;",
                        title="Datos básicos",
                        css_class="w-1/3 mx-1 px-2 py-2 form-group"
                    ),
                    Column(
                        HTML('<h2 class="my-2 py-1 text-xl font-bold text-white bg-blue-400 rounded-lg text-center">Datos secundarios</h2>'),
                        'image', 'gender', 'civil_status', 'person_type', 
                        Field('date_of_birth'), 'budget_capacity', 'additional_info',
                        style="margin-bottom: 5px; border: 2px solid #a4a5a5;",
                        title="Datos adicionales",
                        css_class="w-1/3 mx-1 px-2 py-2 form-group"
                    ),
                    Column(
                        HTML('<h2 class="my-2 py-1 text-xl font-bold text-white bg-blue-400 rounded-lg text-center">Datos de ubicación</h2>'),
                        'res_city', 'address', 
                        HTML('<h2 class="my-2 py-1 text-xl font-bold text-white bg-blue-400 rounded-lg text-center">Datos laborales</h2>'),
                        'academic_level', 'work_type', 'work_industry', 'work_position', 'company_name',
                        style="margin-bottom: 5px; border: 2px solid #a4a5a5;",
                        title="Datos adicionales",
                        css_class="w-1/3 mx-1 px-2 py-2 form-group"
                    ),
                ),
                Submit('submit', 'Guardar', css_class='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded items-center justify-center'),
                css_class="flex justify-center"
            ),
        )
        
    def clean(self):
        cleaned_data = super().clean()
        id_number = self.cleaned_data.get("id_number")

        # Veamos si ya existe su versión sin RUC o en PP
        if (len(str(id_number)) in [10,13]) and id_number.isdigit() and Client.objects.filter(id_number=id_number[:10]).exists():
            raise forms.ValidationError("El número de identificación ya existe")
        elif Client.objects.filter(id_number=id_number).exists():
            raise forms.ValidationError("El número de identificación ya existe")

        try:
            # Natural person ID / RUC validation
            # If not -> PP by defaultpdb.set_trace()
            if (len(str(id_number)) in [10,13]) and id_number.isdigit():
                if (int(id_number[:2]) > 0) and (int(id_number[:2]) <= 24):
                    id_val = str(id_number)[:10]
                    multipy = [2,1,2,1,2,1,2,1,2]
                    sum = 0
                    for num in range(len(multipy)):
                        coef = int(id_val[num]) * multipy[num]
                        if coef >= 10:
                            coef -= 9
                        sum = sum + coef
                    if sum % 10 != 0:
                        # Último paso a validar, el dígito verificador y el resultado del algoritmo
                        # Solo aplica a CI y RUC de persona natural -> ¿y si es de empresa?
                        validator = 10 - (sum % 10) == int(id_val[-1])
                        if (validator == False) and (int(id_val[2]) in [6,9]) and (len(str(id_number)) == 13) and (id_number[10:] == '001'):
                            # puede ser un RUC de empresas, asignar pero levantar un WARNING!
                            cleaned_data['id_type'] = 'RUC'
                            cleaned_data['id_number'] = id_val
                            print('El RUC ingresado no coincide con el de una persona natural, pero se ha validado como RUC de empresa!')
                            #messages.add_warning(self.request, 'El RUC ingresado no coincide con el de una persona natural, pero se ha validado como RUC de empresa!')
                            #raise forms.Warning('El RUC ingresado no coincide con el de una persona natural, pero se ha validado como RUC de empresa!')
                        elif validator and len(str(id_number)) == 10:
                            cleaned_data['id_type'] = 'CI'
                            cleaned_data['id_number'] = id_val
                        elif validator and len(str(id_number)) == 13 and (id_number[10:] == '001'):
                            cleaned_data['id_type'] = 'RUC'
                            cleaned_data['id_number'] = id_val
                        else:
                            raise forms.ValidationError('El número de ID no es válido, revise!')
                    elif int(id_val[-1]) == 0 and len(str(id_number)) == 10:
                        cleaned_data['id_type'] = 'CI'
                        cleaned_data['id_number'] = id_val
                    elif int(id_val[-1]) == 0 and len(str(id_number)) == 13 and (id_number[10:] == '001'):
                        cleaned_data['id_type'] = 'RUC'
                        cleaned_data['id_number'] = id_val
                else:
                    # si no hubo error al querer comparar los 10 o 13 dígitos, sí o sí vamos a suponer que
                    # SE QUIZO INGRESAR UNA CÉDULA O RUC, PERO ESTE ES NO VÁLIDO
                    raise forms.ValidationError('El número de ID no es válido, revise!')   
            else:
                # si es un número, pero es diferente a 10 y 13, posiblemente sea un pasaporte.
                cleaned_data['id_type'] = 'PP'
        except forms.ValidationError as ve:
            print(f'Error: {str(ve)}')
            raise ve
        except:
            # Si no se pudo convertir a entero, o es una longitud distinta a 10 o 13,  es un pasaporte
            cleaned_data['id_type'] = 'PP'

        return cleaned_data

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if not first_name.isalpha():
            raise forms.ValidationError("El nombre no puede contener números")
        return first_name

    def clean_second_name(self):
        second_name = self.cleaned_data.get("second_name")
        if second_name and not second_name.isalpha():
            raise forms.ValidationError("El segundo nombre no puede contener números")
        return second_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if not last_name.isalpha():
            raise forms.ValidationError("El apellido no puede contener números")
        return last_name
    
    def clean_sur_name(self):
        sur_name = self.cleaned_data.get("sur_name")
        if sur_name and not sur_name.isalpha():
            raise forms.ValidationError("El segundo apellido no puede contener números")
        return sur_name


'''
CAN'T modify the ID number, it's a primary key
Can add / modify almost anything else, including id type and
salesman_refer
''' 
class ReadUpdateClientForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = []
        labels = {
            'id_number': 'Número de Identificación',
            'id_type': 'Tipo de Identificación',
            'client_type': 'Tipo de Cliente',
            'first_name': 'Primer Nombre',
            'image': 'Foto del cliente',
            'second_name': 'Segundo Nombre',
            'last_name': 'Primer Apellido',
            'sur_name': 'Segundo Apellido',
            'gender': 'Género',
            'civil_status': 'Estado Civil',
            'phone': 'Teléfono celular',
            'email': 'Correo electrónico',
            'res_city': 'Ciudad / Provincia / País',
            'academic_level': 'Nivel Académico',
            'address': 'Dirección',
            'person_type': 'Tipo de Persona',
            'nationality': 'Nacionalidad',
            'date_of_birth': 'Fecha de Nacimiento',
            'budget_capacity': 'Nivel de gasto',
            'work_industry': 'Sector ocupacional',
            'work_position': 'Cargo de Trabajo',
            'company_name': 'Nombre de la Empresa',
            'additional_info': 'Información Adicional',
            'work_type': 'Tipo de Trabajo',
        }
     
    id_number = forms.CharField(
        label='Número de Identificación',
        disabled=True,
        widget=forms.HiddenInput(),
    )

    date_of_birth = forms.DateField(
        label='Fecha de Nacimiento',
        widget=forms.SelectDateWidget(attrs={
            'class': 'pointer-events-none opacity-50',
            'style': 'width: 30%; margin-left: 0.25rem; background-color: white; border-radius: 0.5rem; border: 1px solid #D1D5DB; padding-top: 0.5rem; padding-bottom: 0.5rem; padding-left: 0.2rem; padding-right: 0.2rem;',},
            years=range(1880, 2030),
            empty_label=("Año", "Mes", "Día"),
        ),
        required=False,
    )

    gender = forms.ChoiceField(
        label='Género',
        widget=forms.RadioSelect(),
        choices=GENDER_CHOICES,
        required=False,
    )

    id_type = forms.ChoiceField(
        label='Tipo de Identificación',
        choices=ID_TYPE_CHOICES,
        widget=forms.RadioSelect(),
    )

    person_type = forms.ChoiceField(
        label='Tipo de Persona',
        choices=PERSON_TYPE_CHOICES,
        widget=forms.RadioSelect(),
        required=False,
    )

    civil_status = forms.ChoiceField(
        label='Estado Civil',
        choices=CIVIL_STATUS_CHOICES,
        widget=forms.RadioSelect(),
        required=False,
    )

    budget_capacity = forms.ChoiceField(
        label='Nivel de gasto',
        choices=BUDGET_CAPACITY_CHOICES,
        widget=forms.RadioSelect(),
        required=False,
    )

    address = forms.Field(
        label='Dirección',
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False,
    )

    additional_info = forms.Field(
        label='Información Adicional',
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False,
    )

    client_type = forms.ChoiceField(
        label='Tipo de Cliente',
        choices=CLIENT_TYPE_CHOICES,
        widget=forms.RadioSelect(),
        required=False,
    )

    phone = PhoneNumberField(
        label='Teléfono celular',
        widget=PhoneNumberPrefixWidget(
            number_attrs={'class': 'pointer-events-none opacity-50 ml-1 form-control bg-white rounded-lg border border-gray-300 py-2 px-4',
                          'style': 'width: 45%;'},
            country_attrs={'class': 'pointer-events-none opacity-50 mr-1 form-control bg-white rounded-lg border border-gray-300 py-2 px-2',
                            'style': 'width: 45%;'},)
        )

    res_city = s2forms.ModelSelect2Widget(
        queryset=cache.get_or_set('cached_cities', cities_light.models.City.objects.all(), 60*60*2),
        attrs={
            'data-minimum-input-length': 2,
            'data-placeholder': 'Buscar ciudad',
            'data-close-on-select': 'true',
        },
    )
    
    image = forms.ImageField(
        label='Foto del cliente',
        required= False,
    )

    salesman_refer = forms.ModelChoiceField(
        label='Vendedor referente',
        queryset=UserProfile.objects.all(),
        widget=forms.Select()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_class='block text-xs font-bold mb-2'
        self.helper.layout = Layout(
            Field(
                Row(
                    Column(
                        #The image, fullname, id number and edit button\
                        Div(
                            Field('image',
                                  css_class="pointer-events-none opacity-50",
                                  id='editable',),
                            css_class="w-full px-2 py-2 mb-2 form-group rounded-lg border-2 border-gray-500 bg-gray-50"
                        ),
                        Div(
                            HTML('<h2 class="mb-2 text-l font-bold text-white bg-blue-400 rounded-lg text-center">Número de identificación</h2>'),
                            HTML('<p class="mb-2 text-xl font-bold text-center">{{ form.id_number.value }}</p>'),
                            css_class="px-2 py-2 mb-2 form-group rounded-lg border-2 border-gray-500 bg-gray-50",
                        ),
                        Div(
                            HTML('<h2 class="mb-2 text-l font-bold text-white bg-blue-400 rounded-lg text-center">Nombre del cliente</h2>'),
                            Div(
                                Field('first_name', id='editable', css_class='mr-2 pointer-events-none opacity-50'), 
                                Field('second_name', id='editable', css_class='mr-2 pointer-events-none opacity-50', ),
                                Field('last_name', id='editable', css_class='mr-2 pointer-events-none opacity-50'),
                                Field('sur_name', id='editable', css_class='mr-2 pointer-events-none opacity-50'),
                                css_class="grid grid-cols-2 gap-2 ",
                                style="font-size: 1em; font: bold;",
                            ),
                            css_class="px-2 py-2 mb-2 form-group rounded-lg border-2 border-gray-500 bg-gray-50",
                        ),
                        Div(
                            Button('edit', 'Editar', css_id='edit-button', 
                                   style='width: 45%;', css_class='text-l bg-blue-500 hover:bg-blue-700 text-white font-bold py-3 px-4 rounded items-center justify-center text-center'),
                            Submit('submit', 'Guardar', css_id='submit-button', 
                                   style='display: none; width: 45%;', css_class='text-l bg-green-500 hover:bg-green-700 text-white font-bold py-3 px-4 rounded items-center justify-center text-center'),
                            HTML('<a href="{% url "clients" %}" style="width: 45%;" class="text-l bg-yellow-400 hover:bg-yellow-600 text-white font-bold py-3 px-4 rounded items-center justify-center text-center">Regresar</a>'),
                            css_class="flex justify-around align-center my-5",
                        ),
                        css_class="w-1/3 mx-1 px-2 py-2 form-group bg-gray-600",
                    ),
                    Column(
                        #The divs with different fields to been displayed
                        Row(
                            Div(
                                Field('phone', id='editable',), 
                                Field('email', id='editable', css_class='pointer-events-none opacity-50'), 
                                Field('id_type', id='editable', css_class='pointer-events-none opacity-50'), 
                                Field('date_of_birth', id='editable', css_class='pointer-events-none opacity-50'), 
                                Field('client_type', id='editable', css_class='pointer-events-none opacity-50'), 
                                Field('salesman_refer', id='editable', css_class='pointer-events-none opacity-50'), 
                                Field('additional_info', id='editable', css_class='pointer-events-none opacity-50'),
                                css_class='w-1/2 mx-1 px-2 py-2 form-group border-2 rounded-lg border-gray-500 bg-gray-50',
                            ),
                            Div(
                                Field('gender', id='editable', css_class='pointer-events-none opacity-50'), 
                                Field('civil_status', id='editable', css_class='pointer-events-none opacity-50'), 
                                Field('person_type', id='editable', css_class='pointer-events-none opacity-50'), 
                                Field('budget_capacity', id='editable', css_class='pointer-events-none opacity-50'),
                                css_class='w-1/2 mx-1 px-2 py-2 form-group border-2 rounded-lg border-gray-500 bg-gray-50'
                            ),
                            css_id='div1',
                            style='display: flex;',
                            css_class='tab-content flex flex-row',
                        ),
                        Row(
                            Div(
                                Field('res_city', id='editable',), 
                                Field('address', id='editable', css_class='pointer-events-none opacity-50'),
                                css_class="mx-1 px-2 py-2 form-group border-2 rounded-lg border-gray-500 bg-gray-50"
                            ),
                            css_id='div2',
                            style='display: none;',
                            css_class='tab-content',
                        ),
                        Row(
                            Div(
                                HTML(
                                    """
                                    <h2 class="text-center text-xl font-bold text-white"> Pasaportes registrados </h2>
                                    {% if not passports %}
                                    <div class="inline-block my-3 w-2/3 text-center px-1 py-1 form-group border-2 rounded-lg border-gray-500 bg-gray-50">
                                        <h2 class="text-l font-bold"> No se ha encontrado ningún pasaporte registrado para este cliente </h2>
                                    </div>    
                                    {% else %}
                                    <div class="grid grid-cols-2 gap-1 mx-1 px-1 py-1 form-group">
                                        {% for passport in passports %}
                                        <div class="text-center px-1 py-1 form-group border-2 rounded-lg border-gray-500 bg-gray-50">
                                            <h2 class="mb-2 text-l font-bold text-white bg-teal-500 rounded-lg text-center">Pasaporte ({{ passport.passport_issue_country }})</h2>
                                            <div class="flex flex-row border-b border-gray-400 my-3">
                                                <label class="w-1/4 text-xs font-bold">Número y tipo: </label>
                                                <p class="w-3/4 text-m font-bold">{{ passport.passport_number }} - {{ passport.passport_type }}</p> 
                                            </div>
                                            <div class="flex flex-row border-b border-gray-400 my-3">
                                                <label class="w-1/4 text-xs font-bold">Fecha de expedición: </label>
                                                <p class="w-3/4 text-m font-bold">{{ passport.passport_issue_date }}</p>
                                            </div>
                                            <div class="flex flex-row border-b border-gray-400 my-3">
                                                <label class="w-1/4 text-xs font-bold">Fecha de expiración: </label>
                                                <p class="w-3/4 text-m font-bold">{{ passport.passport_expire_date }}</p>
                                            </div>
                                            <form action="{% url 'passport_delete' passport.pk %}" method="POST">
                                                {% csrf_token %}
                                                <button id='editable' class="pointer-events-none opacity-50 px-2 py-1 bg-red-500 hover:bg-red-600 text-white rounded-xl"> Eliminar </button>
                                            </form>
                                        </div>
                                        {% endfor %}
                                    </div>
                                    {% endif %}
                                    """
                                ),
                                css_class="my-2 text-center form-group border-2 border-gray-600 bg-gray-500"
                            ),
                            Div(
                                # For items in Passport, display --> first item to show
                                # For items in visa, display --> card template
                                HTML(
                                    """
                                    <h2 class="text-center text-xl font-bold text-white"> Visas registradas </h2>
                                    {% if not visas %}
                                    <div class="inline-block my-3 w-2/3 text-center px-1 py-1 form-group border-2 rounded-lg border-gray-500 bg-gray-50">                                    
                                        <h2 class="text-l font-bold"> No se ha encontrado ninguna visa registrada para este cliente </h2>
                                    </div>
                                    {% else %}
                                    <div class="grid grid-cols-2 gap-1 mx-1 px-1 py-1 form-group">
                                        {% for visa in visas %}
                                        <div class="text-center px-1 py-1 form-group border-2 rounded-lg border-gray-500 bg-gray-50">
                                            <h2 class="mb-2 text-l font-bold text-white bg-teal-500 rounded-lg text-center">Visa ({{ visa.visa_to_country }})</h2>
                                            <div class="flex flex-row border-b border-gray-400 my-3">
                                                <label class="w-1/4 text-xs font-bold">Número y tipo: </label>
                                                <p class="w-3/4 text-m font-bold">{{ visa.visa_number }} - {{ visa.visa_type }}</p> 
                                            </div>
                                            <div class="flex flex-row border-b border-gray-400 my-3">
                                                <label class="w-1/4 text-xs font-bold">Fecha de expedición: </label>
                                                <p class="w-3/4 text-m font-bold">{{ visa.visa_issue_date }}</p>
                                            </div>
                                            <div class="flex flex-row border-b border-gray-400 my-3">
                                                <label class="w-1/4 text-xs font-bold">Fecha de expiración: </label>
                                                <p class="w-3/4 text-m font-bold">{{ visa.visa_expire_date }}</p>
                                            </div>
                                            <form action="{% url 'visa_delete' visa.pk %}" method="POST">
                                                {% csrf_token %}
                                                <button id='editable' class="pointer-events-none opacity-50 px-2 py-1 bg-red-500 hover:bg-red-600 text-white rounded-xl"> Eliminar </button>
                                            </form>
                                        </div>
                                        {% endfor %}
                                    </div>
                                    {% endif %}
                                    """
                                ),
                                css_class="my-2 text-center form-group border-2 border-gray-600 bg-gray-500"
                            ),                            
                            Div(
                                HTML('''<a id="editable" href="{% url "visa_create" client.id_number %}" style="width: 45%;" 
                                     class="pointer-events-none opacity-50 text-l bg-green-400 hover:bg-green-600 text-white font-bold py-3 px-4 rounded items-center justify-center text-center">Nueva Visa</a>'''),
                                HTML('''<a id="editable" href="{% url "passport_create" client.id_number %}" style="width: 45%;" 
                                     class="pointer-events-none opacity-50 text-l bg-yellow-400 hover:bg-yellow-600 text-white font-bold py-3 px-4 rounded items-center justify-center text-center">Nuevo Pasaporte</a>'''),
                                css_class="flex justify-around align-center my-5",
                            ),
                            css_id='div3',
                            style='display: none;',
                            css_class='tab-content flex flex-col',
                        ),
                        Row(
                            Div(
                                Field('academic_level', id='editable', css_class='pointer-events-none opacity-50'), 
                                Field('work_type', id='editable', css_class='pointer-events-none opacity-50'), 
                                Field('work_industry', id='editable', css_class='pointer-events-none opacity-50'), 
                                Field('work_position', id='editable', css_class='pointer-events-none opacity-50'), 
                                Field('company_name', id='editable', css_class='pointer-events-none opacity-50'),
                                css_class=" mx-1 px-2 py-2 form-group border-2 rounded-lg border-gray-500 bg-gray-50"
                            ),
                            css_id='div4',
                            style='display: none;',
                            css_class='tab-content',
                        ),
                        css_class="justify-center items-center flex w-1/2 mx-1 px-2 py-2 form-group bg-gray-300",
                    ),
                    Column(
                        Button('edit', 'Información general', 
                               css_class='show-div my-4 text-l bg-white text-black font-bold py-3 px-2 rounded items-center justify-center text-center', 
                               data_target='#div1'),
                        Button('edit', 'Información de domicilio', 
                               css_class='show-div my-4 text-l bg-gray-500 text-white font-bold py-3 px-2 rounded items-center justify-center text-center', 
                               data_target='#div2'),
                        Button('edit', 'Información de viaje', 
                               css_class='show-div my-4 text-l bg-gray-500 text-white font-bold py-3 px-2 rounded items-center justify-center text-center', 
                               data_target='#div3'),
                        Button('edit', 'Información laboral', 
                               css_class='show-div my-4 text-l bg-gray-500 text-white font-bold py-3 px-2 rounded items-center justify-center text-center', 
                               data_target='#div4'),
                        css_class='w-15 mx-1 px-2 py-2 form-group bg-gray-600 flex flex-col items-stretch text-sm',
                    ),
                ),

            ),
        )

    def clean_id_number(self):
        # Validar si el id_number ha cambiado
        old_id_number = self.instance.id_number
        new_id_number = self.cleaned_data['id_number']
        if old_id_number != new_id_number:
            raise forms.ValidationError('No se permite cambiar el número de identificación.')
        return new_id_number


'''
Visa form -> an average form that will also use the user
picture (desirable feature to have) and will have the same
or similar distribution as a normal visa
'''
class AddVisaForm(forms.ModelForm):
    class Meta:
        model = Visa
        exclude = []
        labels = {
            'visa_holder': 'Titular de la visa',
            'visa_type': 'Tipo de visa',
            'visa_number': 'Número de visa',
            'visa_issue_date': 'Fecha de emisión',
            'visa_expire_date': 'Fecha de expiración',
            'visa_to_country': 'País de destino',
        }

    visa_issue_date = forms.DateField(
        label='Fecha de emisión',
        widget=forms.SelectDateWidget(attrs={
            'style': 'width: 32%; margin-left: 0.25rem; background-color: white; border-radius: 0.5rem; border: 1px solid #D1D5DB; padding-top: 0.5rem; padding-bottom: 0.5rem; padding-left: 0.2rem; padding-right: 0.2rem;',},
            years=range(2000, 2030),
            empty_label=("Año", "Mes", "Día"),
        ),
    )

    visa_expire_date = forms.DateField(
        label='Fecha de expiración',
        widget=forms.SelectDateWidget(attrs={
            'style': 'width: 32%; margin-left: 0.25rem; background-color: white; border-radius: 0.5rem; border: 1px solid #D1D5DB; padding-top: 0.5rem; padding-bottom: 0.5rem; padding-left: 0.2rem; padding-right: 0.2rem;',},
            years=range(2000, 2030),
            empty_label=("Año", "Mes", "Día"),
        ),
    )

    visa_to_country = s2forms.ModelSelect2Widget(
        label='País de destino',
    )

    visa_holder = forms.ModelChoiceField(
        queryset=Client.objects.all(),
        widget=forms.HiddenInput(),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field(
                Row(
                    Column(
                        HTML('<h2 class="my-2 py-1 text-xl font-bold text-white bg-blue-400 rounded-lg text-center">Nueva visa para: {{ client.first_name }} {{ client.last_name }} ({{ form.visa_holder.value }})</h2>'),
                        Field('visa_holder',),                        
                        Field('visa_type',),
                        Field('visa_number',),
                        Field('visa_issue_date',), 
                        Field('visa_expire_date',), 
                        Field('visa_to_country',
                              css_class="form-group mx-1 px-2 py-2",),
                        css_class="mx-1 px-2 py-2 form-group",
                    ),
                    Submit('submit', 'Guardar', 
                        css_class='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded items-center justify-center',
                    ),
                    css_class="flex flex-col justify-center",
                ),
            ),
        )


'''
Passport form -> an average form that will also use the user
picture (desirable feature to have) and will have the same
or similar distribution as a normal passport
'''
class AddPassportForm(forms.ModelForm):
    class Meta:
        model = Passport
        fields = '__all__'
        labels = {
            'passport_holder': 'Titular del pasaporte',
            'passport_number': 'Número de pasaporte',
            'passport_issue_date': 'Fecha de emisión',
            'passport_expire_date': 'Fecha de expiración',
            'passport_issue_country': 'País de emisión',
            'passport_type': 'Tipo de pasaporte',
        }
    
    passport_holder = forms.ModelChoiceField(
        queryset=Client.objects.all(),
        widget=forms.HiddenInput(),
    )

    passport_issue_date = forms.DateField(
        label='Fecha de emisión',
        widget=forms.SelectDateWidget(attrs={
            'style': 'width: 32%; margin-left: 0.25rem; background-color: white; border-radius: 0.5rem; border: 1px solid #D1D5DB; padding-top: 0.5rem; padding-bottom: 0.5rem; padding-left: 0.2rem; padding-right: 0.2rem;',},
            years=range(2000, 2030),
            empty_label=("Año", "Mes", "Día"),
        ),
    )

    passport_expire_date = forms.DateField(
        label='Fecha de expiración',
        widget=forms.SelectDateWidget(attrs={
            'style': 'width: 32%; margin-left: 0.25rem; background-color: white; border-radius: 0.5rem; border: 1px solid #D1D5DB; padding-top: 0.5rem; padding-bottom: 0.5rem; padding-left: 0.2rem; padding-right: 0.2rem;',},
            years=range(2000, 2030),
            empty_label=("Año", "Mes", "Día"),
        ),
    )

    passport_issue_country = s2forms.ModelSelect2Widget(
        label='País de origen del pasaporte',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field(
                Row(
                    Column(
                        HTML('<h2 class="my-2 py-1 text-xl font-bold text-white bg-blue-400 rounded-lg text-center">Nuevo pasaporte para: {{ client.first_name }} {{ client.last_name }} ({{ form.passport_holder.value }})</h2>'),
                        Field('passport_holder',),                        
                        Field('passport_type',),
                        Field('passport_number',),
                        Field('passport_issue_date',), 
                        Field('passport_expire_date',), 
                        Field('passport_issue_country',
                              css_class="form-group mx-1 px-2 py-2",),
                        css_class="mx-1 px-2 py-2 form-group",
                    ),
                    Submit('submit', 'Guardar', 
                        css_class='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded items-center justify-center',
                    ),
                    css_class="flex flex-col justify-center",
                ),
            ),
        )