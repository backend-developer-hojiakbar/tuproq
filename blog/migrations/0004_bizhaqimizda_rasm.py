# Generated by Django 4.2.3 on 2023-09-11 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_yangiliklar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bizhaqimizda_rasm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.ImageField(upload_to='rasmlar/images')),
                ('nom', models.CharField(max_length=200)),
            ],
        ),
    ]
