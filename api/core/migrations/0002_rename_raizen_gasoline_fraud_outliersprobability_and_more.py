# Generated by Django 4.1 on 2022-11-30 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='raizen_gasoline_fraud',
            new_name='OutliersProbability',
        ),
        migrations.AlterModelTable(
            name='outliersprobability',
            table='raizen_gasoline_fraud',
        ),
    ]
