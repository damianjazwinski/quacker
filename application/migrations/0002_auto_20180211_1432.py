# Generated by Django 2.0.2 on 2018-02-11 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image_link',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='image_link'),
        ),
    ]