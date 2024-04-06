
# Dictionaries for metadata fields

WORK_TYPE_CHOICES =[
    ('I', 'Independiente'),
    ('D', 'Dependiente'),
    ]

GENDER_CHOICES =[
    ('M', 'Masculino'), 
    ('F', 'Femenino'), 
    ('O', 'Otro')
    ]

CIVIL_STATUS_CHOICES = [
    ('s', 'Soltero(a)'), 
    ('c', 'Casado(a)'), 
    ('d', 'Divorciado(a)'), 
    ('v', 'Viudo(a)'),
    ]

ID_TYPE_CHOICES = [
    ('CI', 'CI'),
    ('RUC', 'RUC'),
    ('PP', 'Pasaporte'),
    ]

CLIENT_TYPE_CHOICES = [
    ('P', 'prospecto'),
    ('C', 'cliente'),
    ]

PERSON_TYPE_CHOICES = [
    ('N', 'Natural'),
    ('J', 'Jurídica'),
    ]

BUDGET_CAPACITY_CHOICES = [
    ('l', 'Bajo'),
    ('ml', 'Medio-bajo'),
    ('m', 'Medio'),
    ('mh', 'Medio-alto'),
    ('h', 'Alto'),
    ]

WORK_INDUSTRY_CHOICES = [
    ('AGRI', 'Agricultura'),
    ('ARTS', 'Arte'),
    ('BSNS', 'Negocios'),
    ('COMM', 'Comunicación'),
    ('TECH', 'Ciencias computacionales / Tecnología'),
    ('HLTH', 'Salud / Medicina'),
    ('EDUC', 'Educación'),
    ('FOOD', 'Alimentos / Servicios culinarios'),
    ('ENGR', 'Ingeniería'),
    ('GOVT', 'Gobierno'),
    ('HMKR', 'Amo(a) de casa'),
    ('LEGL', 'Servicios legales'),
    ('MLTY', 'Servicios militares'),
    ('SCNC', 'Ciencias naturales'),
    ('UNPY', 'Sin empleo'),
    ('PYSI', 'Deportes / Actividad física'),
    ('RLGN', 'Servicios religiosos'),
    ('RSCH', 'Investigación'),
    ('RTRD', 'Jubilado(a)'),
    ('STDN', 'Estudiante'),
    ('OTHR', 'Otro(s)')
]

ACADEMIC_LEVEL_CHOICES = [
    ('PR', 'Primaria'),
    ('HS', 'Secundaria'),
    ('SU', 'Superior'),
    ('PG', 'Posgrado'),
    ]

VISA_TYPE_CHOICES = [
    ('TRS', 'Visa de turista ()'),
    ('STU', 'Visa de estudiante ()'),
    ('WRK', 'Visa de trabajo ()'),
    ('BSN', 'Visa de negocios ()'),
    ('FAM', 'Visa familiar ()'),
    ('TRA', 'Visa de tránsito ()'),
    ('DIP', 'Visa diplomática ()'),
    ('OFF', 'Visa oficial ()'),
    ('REL', 'Visa religiosa ()'),
    ('MED', 'Visa médica ()'),
    ('REF', 'Visa de refugiado ()'),
    ('IMM', 'Visa de inmigrante ()'),
    ]

PASSPORT_TYPE_CHOICES = [
    ('TRS', 'Visa de turista ()'),
    ('STU', 'Visa de estudiante ()'),
    ('WRK', 'Visa de trabajo ()'),
    ('BSN', 'Visa de negocios ()'),
    ('FAM', 'Visa familiar ()'),
    ('TRA', 'Visa de tránsito ()'),
    ('DIP', 'Visa diplomática ()'),
    ('OFF', 'Visa oficial ()'),
    ('REL', 'Visa religiosa ()'),
    ('MED', 'Visa médica ()'),
    ('REF', 'Visa de refugiado ()'),
    ('IMM', 'Visa de inmigrante ()'),
    ]