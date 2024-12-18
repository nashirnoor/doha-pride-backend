# Generated by Django 4.2 on 2024-11-07 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0026_tourbooking_created_transferbooking_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourbooking',
            name='currency',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='tourbooking',
            name='payment_type',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='transferbooking',
            name='currency',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='transferbooking',
            name='payment_type',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
