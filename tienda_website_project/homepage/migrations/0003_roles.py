# Generated by Django 4.2.4 on 2023-10-16 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_alter_registros_usuarios_apellidos_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='roles',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False)),
                ('rol', models.CharField(max_length=50, verbose_name='Rol')),
            ],
        ),
    ]
