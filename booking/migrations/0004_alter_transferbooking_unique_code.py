# Generated by Django 4.2 on 2024-10-20 14:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_transferbooking_flight_transferbooking_hotel_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transferbooking',
            name='unique_code',
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True, unique=True),
        ),
    ]
