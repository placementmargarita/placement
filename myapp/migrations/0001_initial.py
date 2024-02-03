# Generated by Django 4.2.7 on 2023-12-28 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=300)),
                ('prix', models.FloatField(blank=True, max_length=10)),
                ('employeur', models.CharField(blank=True, max_length=50)),
                ('horaire', models.CharField(blank=True, max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
