# Generated by Django 4.2.6 on 2023-11-03 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Professor', '0007_officehours_office_alter_appointment_professor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officehours',
            name='Day',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Sunday'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday')]),
        ),
    ]
