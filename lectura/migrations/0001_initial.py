# Generated by Django 5.1.5 on 2025-02-01 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lectura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=200)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('resumen', models.TextField()),
            ],
        ),
    ]
