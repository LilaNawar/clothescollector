# Generated by Django 4.0.3 on 2022-03-28 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_cat_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='image',
            field=models.CharField(blank=True, default=None, max_length=2000, null=True),
        ),
    ]