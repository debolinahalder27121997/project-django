# Generated by Django 3.1.1 on 2020-09-28 04:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='emptime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(default='', max_length=100)),
                ('ename', models.CharField(default='', max_length=100)),
                ('edate', models.DateField(blank=True, null=True)),
                ('entrytime', models.TimeField(blank=True, null=True)),
                ('exittime', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='leavedetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(default='', max_length=100)),
                ('ename', models.CharField(default='', max_length=100)),
                ('leave_type', models.CharField(max_length=100)),
                ('total_leave', models.IntegerField(default='')),
                ('sdate', models.DateField(blank=True, null=True)),
                ('edate', models.DateField(blank=True, null=True)),
                ('reason', models.CharField(default='', max_length=200)),
                ('approval', models.CharField(default='', max_length=3)),
            ],
            options={
                'db_table': 'leave',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(max_length=100)),
                ('doj', models.DateField(auto_now_add=True)),
                ('address', models.CharField(default='', max_length=200)),
                ('pic', models.ImageField(default='', upload_to='media/')),
                ('phone', models.CharField(default='', max_length=12)),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'office',
            },
        ),
    ]
