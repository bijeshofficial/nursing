# Generated by Django 4.2.2 on 2023-07-15 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_jobpost_deadline_jobpost_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='role_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='job_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
