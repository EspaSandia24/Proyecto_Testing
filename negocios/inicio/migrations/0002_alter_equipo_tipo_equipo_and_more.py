# Generated by Django 4.1.6 on 2023-12-11 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='tipo_equipo',
            field=models.CharField(choices=[('E', 'Escritorio-CPU'), ('P', 'Portatil'), ('A', 'AIO'), ('I', 'Impresora'), ('M', 'Multifuncional'), ('T', 'Tablet')], default='P', max_length=1),
        ),
        migrations.AlterField(
            model_name='ordenservicio',
            name='id_orden',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]