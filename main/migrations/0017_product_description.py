# Generated by Django 4.0 on 2022-05-27 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_product_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='None', max_length=2000, verbose_name='Product description'),
        ),
    ]