# Generated by Django 3.2.8 on 2023-04-28 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0004_delete_vacuna'),
    ]

    operations = [
        migrations.CreateModel(
            name='vacunas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, null=True, verbose_name='Nombres')),
            ],
        ),
    ]
