# Generated by Django 4.2.11 on 2024-04-11 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appEmpresaDjango', '0002_alter_departamento_options_alter_empleado_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='habilidades',
            new_name='habilidad',
        ),
        migrations.AlterField(
            model_name='departamento',
            name='nombre',
            field=models.CharField(max_length=60),
        ),
    ]
