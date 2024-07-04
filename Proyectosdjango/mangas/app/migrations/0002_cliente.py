# Generated by Django 5.0.6 on 2024-07-04 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(max_length=50)),
                ('rut', models.CharField(max_length=10, null=True)),
                ('direccion', models.CharField(max_length=50, null=True)),
                ('telefono', models.CharField(max_length=12, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
