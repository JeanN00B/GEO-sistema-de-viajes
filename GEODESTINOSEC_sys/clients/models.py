from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
PROVINCES_CITIES_ECUADOR = {
    "Azuay": ["Cuenca", "Gualaceo", "Sigsig", "Chordeleg", "Girón", "Paute", "Santa Isabel", "Sevilla de Oro", "Nabón", "San Fernando"],
    "Bolívar": ["Guaranda", "Chillanes", "Chimbo", "Echeandía", "San Miguel", "Caluma", "Las Naves"],
    "Cañar": ["Azogues", "Biblián", "Cañar", "La Troncal", "El Tambo", "Déleg"],
    "Carchi": ["Tulcán", "Bolívar", "Espejo", "Mira", "Montúfar", "San Pedro de Huaca"],
    "Chimborazo": ["Riobamba", "Alausí", "Colta", "Guamote", "Chambo", "Chunchi", "Cumandá", "Guano", "Pallatanga", "Penipe"],
    "Cotopaxi": ["Latacunga", "La Maná", "Pangua", "Pujilí", "Salcedo", "Saquisilí", "Sigchos"],
    "El Oro": ["Machala", "Arenillas", "Atahualpa", "Balsas", "Chilla", "El Guabo", "Huaquillas", "Marcabelí", "Pasaje", "Piñas", "Portovelo", "Santa Rosa", "Zaruma"],
    "Esmeraldas": ["Esmeraldas", "Eloy Alfaro", "Muisne", "Quinindé", "San Lorenzo"],
    "Galápagos": ["San Cristóbal", "Isabela", "Santa Cruz"],
    "Guayas": ["Guayaquil", "Alfredo Baquerizo Moreno (Jujan)", "Balao", "Balzar", "Colimes", "Coronel Marcelino Maridueña", "Daule", "Durán", "El Empalme", "El Triunfo", "Milagro", "Naranjal", "Naranjito", "Palestina", "Pedro Carbo", "Playas", "Samborondón", "Santa Lucía", "Simón Bolívar", "Yaguachi"],
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
    "Santo Domingo": ["Santo Domingo", "La Concordia"],
    "Sucumbíos": ["Nueva Loja", "Cascales", "Cuyabeno", "Gonzalo Pizarro", "Putumayo", "Shushufindi", "Sucumbíos"],
    "Tungurahua": ["Ambato", "Baños de Agua Santa", "Cevallos", "Mocha", "Patate", "Quero", "Pelileo", "Pillaro", "Quisapincha", "Tisaleo"],
    "Zamora Chinchipe": ["Zamora", "Centinela del Cóndor", "Chinchipe", "El Pangui", "Nangaritza", "Palanda", "Paquisha", "Yacuambi", "Yantzaza"],
    }
# Select all primary keys and makes a list of provinces to use in the province field
PROVINCES_CHOICES = [
    (province, province.capitalize()) for province in PROVINCES_CITIES_ECUADOR.keys()
    ]
# All available cities in Ecuador, to validate the city field
CITIES_CHOICES = [
    (city, city.capitalize()) for cities in PROVINCES_CITIES_ECUADOR.values() for city in cities
    ]
GENDER_CHOICES =[
    ('M', 'Masculino'), 
    ('F', 'Femenino'), 
    ('O', 'Otro')
    ]
CIVIL_STATUS_CHOICES = [
    ('s', 'Soltero'), 
    ('c', 'Casado'), 
    ('d', 'Divorciado'), 
    ('v', 'Viudo'),
    ]
ID_TYPE_CHOICES = [
    ('CI', 'CI'),
    ('RUC', 'RUC'),
    ]
CLIENT_TYPE_CHOICES = [
    ('P', 'prospecto'),
    ('C', 'cliente'),
    ]
PERSON_TYPE_CHOICES = [
    ('N', 'Natural'),
    ('J', 'Jurídica'),
    ]
NATIONALITIES_CHOICES = [
    ("USA", "Estados Unidos"), ("CAN", "Canadá"), ("MEX", "México"), ("UK", "Reino Unido"),
    ("FRA", "Francia"), ("GER", "Alemania"), ("ITA", "Italia"), ("ESP", "España"),
    ("POR", "Portugal"), ("BRA", "Brasil"), ("ARG", "Argentina"), ("CHI", "Chile"),
    ("AUS", "Australia"), ("JPN", "Japón"), ("CHN", "China"), ("IND", "India"),
    ("RSA", "Sudáfrica"), ("EGY", "Egipto"), ("NGA", "Nigeria"), ("KEN", "Kenia"),
    ("RUS", "Rusia"), ("NOR", "Noruega"), ("SWE", "Suecia"), ("FIN", "Finlandia"),
    ("NZL", "Nueva Zelanda"), ("NED", "Países Bajos"), ("BEL", "Bélgica"), ("AUT", "Austria"),
    ("GRE", "Grecia"), ("TUR", "Turquía"), ("IRN", "Irán"), ("IRQ", "Irak"),
    ("SYR", "Siria"), ("THA", "Tailandia"), ("PHI", "Filipinas"), ("KOR", "Corea del Sur"),
    ("PRK", "Corea del Norte"), ("COL", "Colombia"), ("VEN", "Venezuela"),
    ("PER", "Perú"), ("ECU", "Ecuador"), ("CUB", "Cuba"), ("URY", "Uruguay"),
    ("PAR", "Paraguay"), ("BOL", "Bolivia"), ("PAN", "Panamá"), ("CRI", "Costa Rica"),
    ("HON", "Honduras"), ("GTM", "Guatemala"), ("SLV", "El Salvador"), ("NIC", "Nicaragua"),
    ("DOM", "República Dominicana"), ("PRI", "Puerto Rico"), ("JAM", "Jamaica"), ("TTO", "Trinidad y Tobago"),
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
    ("SJM", "Svalbard y Jan Mayen"), ("BVT", "Isla Bouvet"), ("HMD", "Islas Heard y McDonald"), ("ABW", "Aruba"),
    ("CUW", "Curazao"), ("SXM", "Sint Maarten"), ("BES", "Bonaire, San Eustaquio y Saba"), ("JEY", "Jersey"),
    ("GGY", "Guernsey"), ("IMN", "Isla de Man"), ("ESH", "Sáhara Occidental"), ("PLS", "Palesina"),
    ("CHE", "Suiza"), ("NZL", "Nueva Zelanda"), ("MLT", "Malta"), ("IRL", "Irlanda"),
    ("HUN", "Hungría"), ("GRC", "Grecia"), ("FIN", "Finlandia"), ("DNK", "Dinamarca"),
    ("BGR", "Bulgaria"), ("ARM", "Armenia"), ("AND", "Andorra"), ("BEL", "Bélgica"),
    ("DEU", "Alemania"), ("EST", "Estonia"), ("GEO", "Georgia"), ("ITA", "Italia"),
    ("KAZ", "Kazajistán"), ("KGZ", "Kirguistán"), ("LTU", "Lituania"), ("LUX", "Luxemburgo"),
    ("LVA", "Letonia"), ("MDA", "Moldavia"), ("MKD", "Macedonia del Norte"), ("MNE", "Montenegro"),
    ("NLD", "Países Bajos"), ("POL", "Polonia"), ("PRT", "Portugal"), ("ROU", "Rumania"),
    ("RUS", "Rusia"), ("SMR", "San Marino"), ("SRB", "Serbia"), ("SVK", "Eslovaquia"),
    ("SVN", "Eslovenia"), ("SWE", "Suecia"), ("TJK", "Tayikistán"), ("TKM", "Turkmenistán"),
    ("UKR", "Ucrania"), ("UZB", "Uzbekistán"), ("ESP", "España"), ("VAT", "Ciudad del Vaticano"),
    ("ABW", "Aruba"), ("AIA", "Anguila"), ("ASM", "Samoa Americana"), ("BES", "Bonaire, San Eustaquio y Saba"),
    ("BLM", "San Bartolomé"), ("CYM", "Islas Caimán"), ("CUW", "Curazao"), ("FLK", "Islas Malvinas"),
    ("GLP", "Guadalupe"), ("GUM", "Guam"), ("MAF", "San Martín"), ("MTQ", "Martinica"),
    ("MYT", "Mayotte"), ("NIU", "Niue"), ("NFK", "Islas Norfolk"), ("MNP", "Islas Marianas del Norte"),
    ("PYF", "Polinesia Francesa"), ("REU", "Reunión"), ("SHN", "Santa Elena, Ascensión y Tristán de Acuña"),
    ("SPM", "San Pedro y Miquelón"), ("SXM", "Sint Maarten"), ("TCA", "Islas Turcas y Caicos"),
    ("TKL", "Tokelau"), ("UMI", "Islas menores alejadas de los Estados Unidos"), ("VGB", "Islas Vírgenes Británicas"),
    ("VIR", "Islas Vírgenes de los Estados Unidos"), ("WLF", "Wallis y Futuna"), ("VAT", "Santa Sede"),
    ("TWN", "Taiwán"), ("KOS", "Kosovo"),
]
BUDGET_CAPACITY_CHOICES = [
    ('l', 'Bajo'),
    ('ml', 'Medio-bajo'),
    ('m', 'Medio'),
    ('mh', 'Medio-alto'),
    ('h', 'Alto'),
    ]

class Client(models.Model):
    # nro, primary key, 10 o 13 -> validar con algoritmo?
    id_number = models.IntegerField(primary_key=True, null=False, validators=[
        RegexValidator(regex='^\d{10}$', message='La longitud debe ser de 10!', code='nomatch')])
    id_type = models.CharField(max_length=3, null=True, choices=ID_TYPE_CHOICES, default="CI")
    client_type = models.CharField(max_length=2, null=False, choices=CLIENT_TYPE_CHOICES, default='P')

    first_name = models.CharField(max_length=20, null=False)
    second_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, null=False)
    sur_name = models.CharField(max_length=20, blank=True, null=True)
    # Generate the fullname from the first_name, second_name, last_name, and sur_name
    gender = models.CharField(max_length=2, null=True, choices=GENDER_CHOICES, blank=True, default=None)
    civil_status = models.CharField(max_length=2, null=True, 
                                    blank=True, choices=CIVIL_STATUS_CHOICES, default=None)
    # +593 ++ 9 dígitos -> validate! 13 exactly
    phone = models.CharField(max_length=10, null=False, validators=[
        RegexValidator(regex='^09\d{8}$', message='Number must has the 09XXXXXXXX structure', code='nomatch'),
    ])
    email = models.EmailField(max_length=50, null=False, blank=False)
    # SELECT from a list / current session user
    salesman_refer = models.ForeignKey('sysuserprofile.UserProfile', on_delete=models.SET_NULL, null=True, blank=True)  
    province = models.CharField(max_length=20, null=True, blank=True, choices=PROVINCES_CHOICES, default=None)
    # VALIDAR que la ciudad esté en la provincia si no es NULL
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
    #invoice_id = models.IntegerField(max_length=13, null=True, blank=True)
    #has_ruc = models.BooleanField(default=False)    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

    def clean(self):
        #clean añade validaciones adicionales a los campos de un modelo, se llama automáticamente antes de guardar un modelo
        # 1. validate ID + id_type
        if len(str(self.id_number)) != 10:        
            raise ValueError('ID number has to be 10 digits long')

        # 2. validate city in province
        if self.province != None and self.city != None:
            if self.city not in PROVINCES_CITIES_ECUADOR[self.province]:
                raise ValueError('City has to belong to the selected province')
        else:
            pass

    def save(self, *args, **kwargs):
        if len(str(self.id_number)) != 10:        
            raise ValueError('ID number has to be 10 digits long')
        
        # 2. validate city in province
        if self.province != None and self.city != None:
            if self.city not in PROVINCES_CITIES_ECUADOR[self.province]:
                raise ValueError('City has to belong to the selected province')
        else:
            pass
        super().save(*args, **kwargs)