# Generated by Django 3.2.9 on 2022-08-05 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sliced', '0004_auto_20220805_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portofolia',
            name='title',
            field=models.CharField(default=None, max_length=40, unique=True),
        ),
    ]
