# Generated by Django 3.1.1 on 2020-09-29 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20200928_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leavedetail',
            name='approval',
        ),
        migrations.AddField(
            model_name='leavedetail',
            name='status',
            field=models.CharField(default='Pending', max_length=255),
        ),
    ]
