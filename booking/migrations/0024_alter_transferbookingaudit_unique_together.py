# Generated by Django 4.2 on 2024-11-05 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0023_alter_tourbooking_date_alter_tourbooking_name_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='transferbookingaudit',
            unique_together={('transfer_booking', 'action', 'field_name', 'old_value', 'new_value')},
        ),
    ]
