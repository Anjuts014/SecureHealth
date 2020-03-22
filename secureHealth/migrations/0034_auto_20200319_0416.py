# Generated by Django 3.0.3 on 2020-03-19 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secureHealth', '0033_auto_20200319_0409'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminregistrations',
            name='hospital_name',
            field=models.TextField(default='cm hospital'),
        ),
        migrations.AddField(
            model_name='appointmentspage',
            name='hospital_name',
            field=models.TextField(default='cm hospital'),
        ),
        migrations.AddField(
            model_name='departmentdata',
            name='hospital_name',
            field=models.TextField(default='cm hospital'),
        ),
        migrations.AddField(
            model_name='doctordata',
            name='hospital_name',
            field=models.TextField(default='cm hospital'),
        ),
        migrations.AddField(
            model_name='doctorschedule',
            name='hospital_name',
            field=models.TextField(default='cm hospital'),
        ),
        migrations.AddField(
            model_name='employeeadd',
            name='hospital_name',
            field=models.TextField(default='cm hospital'),
        ),
        migrations.AddField(
            model_name='holidaydata',
            name='hospital_name',
            field=models.TextField(default='cm hospital'),
        ),
        migrations.AddField(
            model_name='leavedata',
            name='hospital_name',
            field=models.TextField(default='cm hospital'),
        ),
    ]
