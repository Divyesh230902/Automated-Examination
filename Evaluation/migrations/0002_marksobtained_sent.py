# Generated by Django 3.2.10 on 2022-04-10 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Evaluation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='marksobtained',
            name='sent',
            field=models.BooleanField(default=False),
        ),
    ]
