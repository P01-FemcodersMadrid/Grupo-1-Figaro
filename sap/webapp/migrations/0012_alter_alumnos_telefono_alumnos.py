# Generated by Django 4.0.5 on 2022-07-06 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_remove_profesor_email_profesor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='telefono_alumnos',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
