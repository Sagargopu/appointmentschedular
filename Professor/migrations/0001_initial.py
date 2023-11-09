# Generated by Django 4.2.6 on 2023-10-30 22:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('AppointmentId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('Confirmed', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Appointments',
                'ordering': ['Professor', 'Date'],
            },
        ),
        migrations.CreateModel(
            name='OfficeHours',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('Day', models.CharField(choices=[('Sun', 'Sunday'), ('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday')], max_length=3)),
                ('StartTime', models.TimeField()),
                ('EndTime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('First_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Last_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Phone', models.BigIntegerField(blank=True, null=True)),
                ('Office', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name_plural': 'Professors',
                'ordering': ['Last_Name'],
            },
        ),
    ]
