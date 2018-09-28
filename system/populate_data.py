import os, django, random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'system.settings')
django.setup()

from register.models import Personas
from faker import Faker

fakegen = Faker()

def addPersona(N):
    for _ in range(N):

        fake_name = fakegen.name()
        fake_lastname = fakegen.last_name()
        fake_id = fakegen.ean(length=8)
        fake_phone = fakegen.ean(length=8)
        fake_number = fakegen.ean(length=8)
        fake_address = fakegen.address()
        fake_date = fakegen.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=58)

        print(fake_name)

    s = Personas.objects.get_or_create(nombres=fake_name, apellidos = fake_lastname, cedula = fake_id,
                                   telefono = fake_phone, celular = fake_number,
                                   direccion = fake_address, fecha_nac= fake_date)[0]
    s.save
    return s

addPersona(5)
print("Listo!!!")