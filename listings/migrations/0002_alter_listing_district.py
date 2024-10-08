# Generated by Django 4.2 on 2024-09-10 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='district',
            field=models.CharField(choices=[('Central and Western', 'Central and Western'), ('Eastern', 'Eastern'), ('Islands', 'Islands'), ('Kowloon City', 'Kowloon City'), ('Kwai Tsing', 'Kwai Tsing'), ('Kwun Tong', 'Kwun Tong'), ('North', 'North'), ('Sai Kung', 'Sai Kung'), ('Sha Tin', 'Sha Tin'), ('Sham Shui Po', 'Sham Shui Po'), ('Southern', 'Southern'), ('Tai Po', 'Tai Po'), ('Tsuen Wan', 'Tsuen Wan'), ('Tuen Mun', 'Tuen Mun'), ('Wan Chai', 'Wan Chai'), ('Wong Tai Sin', 'Wong Tai Sin'), ('Yau Tsim Mong', 'Yau Tsim Mong'), ('Yuen Long', 'Yuen Long')], max_length=50),
        ),
    ]
