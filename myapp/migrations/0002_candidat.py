# Generated by Django 4.2.7 on 2024-01-03 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='candidat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('cv', models.FileField(upload_to='')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.job')),
            ],
        ),
    ]
