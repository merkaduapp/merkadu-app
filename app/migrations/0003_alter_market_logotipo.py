# Generated by Django 4.2.9 on 2024-02-24 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_market_logotipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='logotipo',
            field=models.ImageField(blank=True, max_length=250, upload_to='static/merkadu', verbose_name='logomarca'),
        ),
    ]
