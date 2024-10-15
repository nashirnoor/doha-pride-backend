# Generated by Django 4.2 on 2024-10-10 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0003_driverfeedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='driverfeedback',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='driver_feedbacks', to=settings.AUTH_USER_MODEL),
        ),
    ]