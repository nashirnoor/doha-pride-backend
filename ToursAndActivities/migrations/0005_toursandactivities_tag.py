# Generated by Django 4.2 on 2024-11-06 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToursAndActivities', '0004_toursandactivities_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='toursandactivities',
            name='tag',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
