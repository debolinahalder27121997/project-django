from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User
from datetime import datetime


class Employee(models.Model):
    eid = models.ForeignKey(User, on_delete=models.CASCADE)
    dept = models.CharField(max_length=100)
    doj = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=200, default='')
    pic = models.ImageField(upload_to='media/', default='')
    phone = models.CharField(max_length=12, default='')

    class Meta:
        db_table = "office"


class leavedetail(models.Model):
    eid = models.ForeignKey(User, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=100)
    total_leave = models.IntegerField(default='')
    sdate = models.DateField(auto_now_add=False, blank=True, null=True)
    edate = models.DateField(auto_now_add=False, blank=True, null=True)
    reason = models.CharField(max_length=200, default='')
    status = models.CharField(max_length=255, default='Pending')

    class Meta:
        db_table = "leave"


class emptime(models.Model):
    eid = models.ForeignKey(User, on_delete=models.CASCADE)
    edate = models.CharField(max_length=255, null=True)
    entrytime = models.CharField(max_length=255, null=True)
    exittime = models.CharField(max_length=255, null=True)

    class meta:
        db_table = "timetable"
