# Generated by Django 4.2 on 2024-10-20 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_populate_unique_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transferbooking',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]