# Generated by Django 3.0.3 on 2020-03-19 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secureHealth', '0032_patientregistrationdatas_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientrecord',
            name='hospital_name',
            field=models.TextField(default='cm hospital'),
        ),
        migrations.AddField(
            model_name='patientregistrationdatas',
            name='hospital_name',
            field=models.TextField(default='cm hospital'),
        ),
    ]
