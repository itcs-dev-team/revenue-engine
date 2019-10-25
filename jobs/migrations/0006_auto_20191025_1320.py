# Generated by Django 2.2.5 on 2019-10-25 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20191025_0008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='featured_job',
        ),
        migrations.AddField(
            model_name='post',
            name='is_featured_job',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='applicationsource',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]