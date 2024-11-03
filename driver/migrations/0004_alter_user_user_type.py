# Generated by Django 4.2 on 2024-11-03 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0003_alter_user_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('admin', 'Admin'), ('driver', 'Driver'), ('customer', 'Customer'), ('staff', 'Staff'), ('travel_agency', 'Travel Agency')], default='customer', max_length=20),
        ),
    ]
