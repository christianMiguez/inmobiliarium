# Generated by Django 4.2.17 on 2025-01-19 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmobiliariumwebsite', '0007_alter_inmueble_zona'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='es_destacado',
            field=models.BooleanField(default=False, help_text='En metros cuadrados'),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='precio',
            field=models.DecimalField(decimal_places=2, help_text='Siempre en pesos', max_digits=14),
        ),
    ]
