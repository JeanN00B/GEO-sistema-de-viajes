from django.db import models

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
    (province, province) for province in PROVINCES_CITIES_ECUADOR.keys()
    ]
# All available cities in Ecuador, to validate the city field
CITIES_CHOICES = [
    city for cities in PROVINCES_CITIES_ECUADOR.values() for city in cities
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
    ('v', 'Viudo')
    ]


class Contact(models.Model):
    contact_code = models.AutoField(primary_key=True, null=False)

    first_name = models.CharField(max_length=20, null=False)
    second_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, null=False)
    sur_name = models.CharField(max_length=20, blank=True, null=True)
    # Generate the fullname from the first_name, second_name, last_name, and sur_name
    
    gender = models.CharField(max_length=2, null=False, 
                              choices=GENDER_CHOICES, default='O')
    civil_status = models.CharField(max_length=2, null=True, 
                                    blank=True, choices=CIVIL_STATUS_CHOICES, default=None)
    
    phone = models.CharField(max_length=13, null=False)
    email = models.EmailField(max_length=50, null=True, blank=True)
    province = models.CharField(max_length=20, null=True, blank=True, choices=PROVINCES_CHOICES)
    city = models.CharField(max_length=20, null=True, blank=True, choices=CITIES_CHOICES)
    address = models.TextField(max_length=100, null=True, blank=True)
    person_type = models.CharField(max_length=2, null=False, choices=[
        ('N', 'Natural'), ('J', 'Jurídica')], default='N')
    invoice_id = models.IntegerField(max_length=13, null=True, blank=True)
    has_ruc = models.BooleanField(default=False)
    refered_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.has_ruc = len(str(self.invoice_id)) == 13 if self.invoice_id else False
        super().save(*args, **kwargs)