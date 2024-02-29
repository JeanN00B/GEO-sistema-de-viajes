from django import forms
from .models import Client
from django.contrib.auth.decorators import login_required


class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["id_number", "id_type", "client_type", "first_name",
                  "second_name", "last_name", "sur_name",
                  "gender", "civil_status", "phone",
                  "email", "province",
                  "city", "address", "person_type", 
                  "nationality", "date_of_birth", "budget_capacity",
                  "work_industry", "work_position", "company_name",
                  "additional_info"
                  ]
        labels = {
            'id_number': 'Número de Identificación',
            'id_type': 'Tipo de Identificación',
            'client_type': 'Tipo de Cliente',
            'first_name': 'Primer Nombre',
            'second_name': 'Segundo Nombre',
            'last_name': 'Primer Apellido',
            'sur_name': 'Segundo Apellido',
            'gender': 'Género',
            'civil_status': 'Estado Civil',
            'phone': 'Teléfono celular',
            'email': 'Correo electrónico',
            'province': 'Provincia',
            'city': 'Ciudad',
            'address': 'Dirección',
            'person_type': 'Tipo de Persona',
            'nationality': 'Nacionalidad',
            'date_of_birth': 'Fecha de Nacimiento',
            'budget_capacity': 'Capacidad de Presupuesto',
            'work_industry': 'Industria de Trabajo',
            'work_position': 'Cargo de Trabajo',
            'company_name': 'Nombre de la Empresa',
            'additional_info': 'Información Adicional',
        }
        '''     
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
        }
        '''
        def __init__(self, *args, **kwargs):
            self.request = kwargs.pop("request", None)
            super(AddClientForm, self).__init__(*args, **kwargs)
            self.fields['id_type'].disabled = True
        
        def clean_id_number(self):
            id_number = self.cleaned_data.get("id_number")
            if Client.objects.filter(id_number=id_number).exists():
                raise forms.ValidationError("El número de identificación ya existe")
            elif len(id_number) != 10:
                raise forms.ValidationError("El número de identificación debe tener 10 dígitos")
            return id_number