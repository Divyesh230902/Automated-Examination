# Generated by Django 3.2.10 on 2022-04-10 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Examination', '0002_answersheet_studentanswersheet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentanswersheet',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
