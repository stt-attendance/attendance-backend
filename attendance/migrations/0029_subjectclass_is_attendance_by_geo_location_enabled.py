# Generated by Django 4.2.7 on 2023-11-27 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0028_alter_subjectclass_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectclass',
            name='is_attendance_by_geo_location_enabled',
            field=models.BooleanField(default=True),
        ),
    ]