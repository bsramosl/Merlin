# Generated by Django 3.2.9 on 2022-03-22 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PrincipalApp', '0005_alter_profesor_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesor',
            name='area',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='materia',
        ),
        migrations.DeleteModel(
            name='Area',
        ),
        migrations.DeleteModel(
            name='Materia',
        ),
    ]
