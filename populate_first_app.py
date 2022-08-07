import os
from re import T
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
import django
django.setup()
import random
from first_app.models import Topic,WebPage,AccessRecord
from faker import Faker
fakegen=Faker()
topics=['Search','Social','Marketplace','News','Games']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t 


def populate(N):
    for entry in range(0,N):
        top=add_topic()
        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()

        webpg=WebPage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        acc_rec=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]


if __name__=='__main__':
    print("Populating script\n")
    populate(100)
    print("Population completed for Topic,WebPage and  AccessRecords models\n")
    