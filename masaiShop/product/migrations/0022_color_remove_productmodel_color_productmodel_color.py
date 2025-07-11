# Generated by Django 5.2.3 on 2025-07-11 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_comment_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='color',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='color',
            field=models.ManyToManyField(related_name='colors', to='product.color'),
        ),
    ]
