# Generated by Django 3.0.4 on 2020-03-23 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secureHealth', '0034_auto_20200319_0416'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientregistrationdatas',
            name='doctor_name',
            field=models.TextField(default='Dr Anitha Samuel'),
        ),
    ]
