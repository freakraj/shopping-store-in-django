# Generated by Django 3.2.5 on 2021-08-05 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210805_2040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extendeduser',
            old_name='phone_num',
            new_name='phone',
        ),
    ]
