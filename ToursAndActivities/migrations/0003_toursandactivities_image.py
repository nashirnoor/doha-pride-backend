# Generated by Django 4.2 on 2024-11-05 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToursAndActivities', '0002_remove_toursandactivities_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='toursandactivities',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='tour_images/'),
        ),
    ]