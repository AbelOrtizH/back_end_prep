# Generated by Django 4.1.5 on 2023-03-07 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('littleLemon', '0003_logger'),
    ]

    operations = [
        migrations.AddField(
            model_name='logger',
            name='last_name',
            field=models.CharField(default='adams', max_length=50),
        ),
        migrations.AlterField(
            model_name='logger',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
