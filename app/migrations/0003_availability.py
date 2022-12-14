# Generated by Django 4.1.1 on 2022-09-18 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_facility_rename_city_hospital_city_delete_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upadated_at', models.DateTimeField(auto_now=True)),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availabilies', to='app.hospital')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availablies', to='app.hospital')),
            ],
        ),
    ]
