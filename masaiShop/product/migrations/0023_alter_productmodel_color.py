# Generated by Django 5.2.3 on 2025-07-11 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_color_remove_productmodel_color_productmodel_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='color',
            field=models.ManyToManyField(related_name='product_color', to='product.color'),
        ),
    ]
