# Generated by Django 5.0.6 on 2024-06-07 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akudapostupat', '0005_alter_university_type_delete_types'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pluses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Плюс',
                'verbose_name_plural': 'Плюсы',
            },
        ),
        migrations.RemoveField(
            model_name='university',
            name='list_of_pluses',
        ),
        migrations.AddField(
            model_name='university',
            name='list_of_pluses',
            field=models.ManyToManyField(blank=True, related_name='pluses', to='akudapostupat.pluses'),
        ),
    ]