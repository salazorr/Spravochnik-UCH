# Generated by Django 5.0.6 on 2024-06-07 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('akudapostupat', '0006_pluses_remove_university_list_of_pluses_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='university',
            name='invite_after_class',
        ),
        migrations.RemoveField(
            model_name='university',
            name='invite_after_exams',
        ),
        migrations.RemoveField(
            model_name='university',
            name='list_of_name_of_university',
        ),
    ]