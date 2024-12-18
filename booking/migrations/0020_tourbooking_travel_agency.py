# Generated by Django 4.2 on 2024-11-03 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0019_transferbooking_travel_agency'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourbooking',
            name='travel_agency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency_booking', to=settings.AUTH_USER_MODEL),
        ),
    ]
