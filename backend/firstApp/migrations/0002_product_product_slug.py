# Generated by Django 4.0.4 on 2022-05-02 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_slug',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]