
from django.db import migrations
from django.apps import apps

from purchase.models import Purchase

def insert_purchase_data(apps, schema_editor):
    purchase_model = apps.get_model('purchase', 'Purchase')
    for row in purchase_model.objects.all():
        print('ok')
        if row.purchase_user == "boss":
            row.purchase_user = "migrator"
            print('save....')
            row.save(update_fields=['purchase_user'])

class Migration(migrations.Migration):
    
    dependencies = [
       ('purchase', '0001_initial')
    ]
    

    operations = [
        migrations.RunPython(insert_purchase_data),
    ]
