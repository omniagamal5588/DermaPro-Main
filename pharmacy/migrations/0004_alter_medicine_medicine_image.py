# Generated by Django 4.1.7 on 2023-05-21 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0003_medicine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='medicine_image',
            field=models.ImageField(upload_to='img', verbose_name='Medicine Image'),
        ),
    ]
