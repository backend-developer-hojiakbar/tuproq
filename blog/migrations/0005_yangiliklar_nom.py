# Generated by Django 4.2.3 on 2023-09-11 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_bizhaqimizda_rasm'),
    ]

    operations = [
        migrations.AddField(
            model_name='yangiliklar',
            name='nom',
            field=models.CharField(default=2, max_length=1000),
            preserve_default=False,
        ),
    ]