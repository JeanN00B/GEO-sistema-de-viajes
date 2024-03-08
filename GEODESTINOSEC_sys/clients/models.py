from django.db import models
from django.contrib import messages
from django.core.validators import RegexValidator
from static.metadata_dictionaries import *

    "El Oro": ["Machala", "Arenillas", "Atahualpa", "Balsas", "Chilla", "El Guabo", "Huaquillas", "Marcabelí", "Pasaje", "Piñas", "Portovelo", "Santa Rosa", "Zaruma"],
    "Esmeraldas": ["Esmeraldas", "Eloy Alfaro", "Muisne", "Quinindé", "San Lorenzo"],
    "Imbabura": ["Ibarra", "Antonio Ante", "Cotacachi", "Otavalo", "Pimampiro", "San Miguel de Urcuquí"],
    "Loja": ["Loja", "Calvas", "Catamayo", "Celica", "Chaguarpamba", "Espíndola", "Gonzanamá", "Macará", "Paltas", "Puyango", "Quilanga", "Saraguro", "Sozoranga", "Zapotillo"],
    "Los Ríos": ["Babahoyo", "Baba", "Buena Fé", "Mocache", "Montalvo", "Palenque", "Puebloviejo", "Quevedo", "Quinsaloma", "Urdaneta", "Valencia", "Ventanas", "Vinces"],
    "Manabí": ["Portoviejo", "Bolívar", "Chone", "El Carmen", "Flavio Alfaro", "Jama", "Jaramijó", "Jipijapa", "Junín", "Manta", "Montecristi", "Paján", "Pedernales", "Pichincha", "Puerto López", "Rocafuerte", "San Vicente", "Santa Ana", "Sucre", "Tosagua", "24 de Mayo"],
    "Morona Santiago": ["Macas", "Gualaquiza", "Huamboya", "Limón Indanza", "Logroño", "Morona", "Pablo Sexto", "Palora", "San Juan Bosco", "Santiago", "Sucúa", "Taisha", "Tiwinza"],
    "Napo": ["Tena", "Archidona", "Carlos Julio Arosemena Tola", "El Chaco", "Quijos"],
    "Orellana": ["Orellana", "Aguarico", "Francisco de Orellana", "La Joya de los Sachas", "Loreto"],
    "Pastaza": ["Puyo", "Arajuno", "Mera", "Santa Clara"],
    "Pichincha": ["Quito", "Cayambe", "Mejía", "Pedro Moncayo", "Pedro Vicente Maldonado", "Puerto Quito", "Rumiñahui", "San Miguel de los Bancos"],
    "Santa Elena": ["Santa Elena", "La Libertad", "Salinas"],
    (province, province.capitalize()) for province in PROVINCES_CITIES_ECUADOR.keys()
    ]
# All available cities in Ecuador, to validate the city field
CITIES_CHOICES = [
    ]
    ('O', 'Otro')
    ]
CIVIL_STATUS_CHOICES = [
    ('s', 'Soltero'), 
    ('c', 'Casado'), 
    ('v', 'Viudo'),
    ]
ID_TYPE_CHOICES = [
    ('RUC', 'RUC'),
CLIENT_TYPE_CHOICES = [
    ('P', 'prospecto'),
    ]
    ('N', 'Natural'),
    ]
    ("USA", "Estados Unidos"), ("CAN", "Canadá"), ("MEX", "México"), ("UK", "Reino Unido"),
    ("POR", "Portugal"), ("BRA", "Brasil"), ("ARG", "Argentina"), ("CHI", "Chile"),
    ("PRK", "Corea del Norte"), ("COL", "Colombia"), ("VEN", "Venezuela"),
    ("PER", "Perú"), ("ECU", "Ecuador"), ("CUB", "Cuba"), ("URY", "Uruguay"),
    ("PAR", "Paraguay"), ("BOL", "Bolivia"), ("PAN", "Panamá"), ("CRI", "Costa Rica"),
    ("HON", "Honduras"), ("GTM", "Guatemala"), ("SLV", "El Salvador"), ("NIC", "Nicaragua"),
    ("HAI", "Haití"), ("BAH", "Bahamas"), ("BRB", "Barbados"), ("SUR", "Surinam"),
    ("GUY", "Guyana"), ("ATG", "Antigua y Barbuda"), ("DMA", "Dominica"), ("LCA", "Santa Lucía"),
    ("KNA", "San Cristóbal y Nieves"), ("VCT", "San Vicente y las Granadinas"), ("GRD", "Granada"), ("ISL", "Islandia"),
    ("MDA", "Moldavia"), ("EST", "Estonia"), ("LVA", "Letonia"), ("LTU", "Lituania"),
    ("SVK", "Eslovaquia"), ("SVN", "Eslovenia"), ("HRV", "Croacia"), ("BIH", "Bosnia y Herzegovina"),
    ("MKD", "Macedonia del Norte"), ("SRB", "Serbia"), ("MNE", "Montenegro"), ("ALB", "Albania"),
    ("AND", "Andorra"), ("MCO", "Mónaco"), ("LIE", "Liechtenstein"), ("LUX", "Luxemburgo"),
    ("MHL", "Islas Marshall"), ("FSM", "Micronesia"), ("PLW", "Palaos"), ("NRU", "Nauru"),
    ("KIR", "Kiribati"), ("TUV", "Tuvalu"), ("TON", "Tonga"), ("WSM", "Samoa"),
    ("VUT", "Vanuatu"), ("CYP", "Chipre"), ("MLT", "Malta"), ("CZE", "República Checa"),
    ("VAT", "Ciudad del Vaticano"), ("STP", "Santo Tomé y Príncipe"), ("TLS", "Timor Oriental"),
    ("SYC", "Seychelles"), ("MUS", "Mauricio"), ("CPV", "Cabo Verde"), ("COM", "Comoras"),
    ("MDG", "Madagascar"), ("MDV", "Maldivas"), ("REU", "Reunión"), ("SHN", "Santa Elena, Ascensión y Tristán de Acuña"),
    ("CCK", "Islas Cocos"), ("CXR", "Isla de Navidad"), ("PCN", "Islas Pitcairn"), ("TKL", "Tokelau"),
    ("WLF", "Wallis y Futuna"), ("ALA", "Islas Åland"), ("FRO", "Islas Feroe"), ("GRL", "Groenlandia"),
    ("GGY", "Guernsey"), ("IMN", "Isla de Man"), ("ESH", "Sáhara Occidental"), ("PLS", "Palesina"),
    ("CHE", "Suiza"), ("NZL", "Nueva Zelanda"), ("MLT", "Malta"), ("IRL", "Irlanda"),
    ("HUN", "Hungría"), ("GRC", "Grecia"), ("FIN", "Finlandia"), ("DNK", "Dinamarca"),

class Client(models.Model):
    # nro, primary key, 10 o passport -> validar con algoritmo?
    id_number = models.CharField(max_length=20, primary_key=True, null=False, validators=[
        RegexValidator(regex='(^\d{10}||^w*)$', message='Error ID/RUC/Pasaporte no válido!', code='nomatch')])
    
    id_type = models.CharField(max_length=3, null=True, choices=ID_TYPE_CHOICES, default=None)
    
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