# Generated by Django 5.2.1 on 2025-05-14 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='estado',
            field=models.CharField(choices=[('Visto', 'Leido'), ('Sin Ver', 'No Leido')], default='Sin Ver', max_length=10),
        ),
    ]
