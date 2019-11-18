# Generated by Django 2.2.6 on 2019-11-06 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosPersona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=35)),
                ('Direccion', models.CharField(max_length=40)),
                ('Telefono', models.IntegerField()),
                ('Mail', models.EmailField(max_length=254)),
                ('Asunto', models.CharField(max_length=20)),
                ('Mensaje', models.CharField(max_length=200)),
            ],
        ),
    ]
