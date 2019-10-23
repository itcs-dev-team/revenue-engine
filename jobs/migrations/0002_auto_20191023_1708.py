# Generated by Django 2.2.5 on 2019-10-23 09:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mysite', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_by',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='job_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.JobType'),
        ),
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mysite.Location'),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.SET_DEFAULT, to='mysite.Status'),
        ),
        migrations.AddField(
            model_name='jobtype',
            name='created_by',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='jobtype',
            name='status',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.SET_DEFAULT, to='mysite.Status'),
        ),
        migrations.AddField(
            model_name='category',
            name='created_by',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.SET_DEFAULT, to='mysite.Status'),
        ),
        migrations.AddField(
            model_name='applicationsource',
            name='created_by',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='applicationsource',
            name='status',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.SET_DEFAULT, to='mysite.Status'),
        ),
        migrations.AddField(
            model_name='application',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mysite.Location'),
        ),
        migrations.AddField(
            model_name='application',
            name='source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobs.ApplicationSource'),
        ),
    ]
