# Generated by Django 4.0.5 on 2022-06-20 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.CharField(default='00,00', max_length=200),
        ),
    ]