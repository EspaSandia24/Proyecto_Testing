# Generated by Django 4.1.6 on 2023-12-12 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0006_alter_equipo_accesorios_equipo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='telefono_cliente',
            field=models.IntegerField(),
        ),
    ]