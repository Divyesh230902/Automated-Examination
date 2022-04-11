# Generated by Django 3.2.10 on 2022-04-11 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dtail', '0002_auto_20220406_2059'),
        ('Examination', '0003_alter_studentanswersheet_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invigilagtor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Examination.exam')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dtail.professor')),
            ],
        ),
    ]
