from django import forms
from .models import Client
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class AddClientForm(forms.ModelForm):
    phone = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial='EC'))
    class Meta:
        model = Client
        exclude = ['salesman_refer']
        labels = {
            'id_number': 'Número de Identificación',
            'id_type': 'Tipo de Identificación',
            'client_type': 'Tipo de Cliente',
            'first_name': 'Primer Nombre',
            'image': 'Foto',
            'second_name': 'Segundo Nombre',
            'last_name': 'Primer Apellido',
            'sur_name': 'Segundo Apellido',
            'gender': 'Género',
            'civil_status': 'Estado Civil',
            'phone': 'Teléfono celular',
            'email': 'Correo electrónico',
            'province': 'Provincia / Estado',
            'city': 'Ciudad de domicilio',
            'address': 'Dirección',
            'person_type': 'Tipo de Persona',
            'nationality': 'Nacionalidad',
            'date_of_birth': 'Fecha de Nacimiento',
            'budget_capacity': 'Nivel de gasto',
            'work_industry': 'Industria de Trabajo',
            'work_position': 'Cargo de Trabajo',
            'company_name': 'Nombre de la Empresa',
            'additional_info': 'Información Adicional',
        }
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'id_type': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(AddClientForm, self).__init__(*args, **kwargs)
        self.initial['id_type'] = 'CI'

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
            # If not -> PP by default
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

class ReadUpdateClientForm(forms.ModelForm):
    phone = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial='EC'))
    class Meta:
        model = Client
        exclude = []
        labels = {
            'id_number': 'Número de Identificación',
            'id_type': 'Tipo de Identificación',
            'client_type': 'Tipo de Cliente',
            'first_name': 'Primer Nombre',
            'second_name': 'Segundo Nombre',
            'last_name': 'Primer Apellido',
            'sur_name': 'Segundo Apellido',
            'image': 'Foto',
            'gender': 'Género',
            'salesman_refer': 'Vendedor Referente',
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
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'id_number': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['id_type'].widget.attrs['readonly'] = True
        self.fields['id_number'].disabled = True

    def clean_id_number(self):
        # Validar si el id_number ha cambiado
        old_id_number = self.instance.id_number
        new_id_number = self.cleaned_data['id_number']
        if old_id_number != new_id_number:
            raise forms.ValidationError('No se permite cambiar el número de identificación.')
        return new_id_number
