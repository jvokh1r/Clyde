# Generated by Django 4.1.1 on 2022-09-15 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='message',
            field=models.CharField(max_length=1000),
        ),
    ]
