# Generated by Django 4.1.7 on 2023-05-20 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacy',
            name='pharmacy_image',
            field=models.ImageField(upload_to='img', verbose_name='Pharmacy Image'),
        ),
    ]
