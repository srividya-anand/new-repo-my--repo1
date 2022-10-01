import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','empfbvproject.settings')
django.setup()
from myapp.models import Employee
from faker import Faker
f=Faker()
def generate_data(n):
    for i in range(n):
        feid=f.random_int(min=1,max=50)
        fename=f.name()
        feage=f.random_int(min=23,max=50)
        feexp=f.random_int(min=0,max=25)
        fesal=f.random_int(min=10000,max=300000)
        e=Employee.objects.get_or_create(eid=feid,ename=fename,eage=feage,eexp=feexp,esal=fesal)
generate_data(30)