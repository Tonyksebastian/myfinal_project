# Generated by Django 4.2.4 on 2024-02-21 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('make_service', '0005_service_booking_vehno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_booking',
            name='slotnumber',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
