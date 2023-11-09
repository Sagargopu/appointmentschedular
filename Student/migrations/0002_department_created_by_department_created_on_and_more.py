# Generated by Django 4.2.6 on 2023-11-03 20:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='created_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='department',
            name='updated_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='student',
            name='created_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='student',
            name='updated_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
