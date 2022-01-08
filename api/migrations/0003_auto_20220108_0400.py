# Generated by Django 3.2.11 on 2022-01-08 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_element_pokemon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='element',
            name='description',
        ),
        migrations.RemoveField(
            model_name='element',
            name='name',
        ),
        migrations.AddField(
            model_name='element',
            name='chinese',
            field=models.CharField(default='一般', max_length=100),
        ),
        migrations.AddField(
            model_name='element',
            name='english',
            field=models.CharField(default='Normal', max_length=100),
        ),
        migrations.AddField(
            model_name='element',
            name='japanese',
            field=models.CharField(default='ノーマル', max_length=100),
        ),
    ]