# Generated by Django 4.2 on 2024-10-20 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_alter_transferbooking_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transferbooking',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transferbooking',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='transferbooking',
            name='number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='transferbooking',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
