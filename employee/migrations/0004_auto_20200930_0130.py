# Generated by Django 3.1.1 on 2020-09-29 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20200930_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emptime',
            name='edate',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='emptime',
            name='entrytime',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='emptime',
            name='exittime',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
