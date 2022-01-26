from django.db import models

# Create your models here.

class Entry(models.Model):
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    system = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    create_time = models.DateTimeField()
    remove_time = models.DateTimeField()

class Key(models.Model):
    uid = models.ForeignKey(Entry, on_delete=models.CASCADE)
    public_key = models.CharField(max_length=24)
    private_key = models.CharField(max_length=128)

class Requests(models.Model):
    uid = models.IntegerField(primary_key=True)
    entry_uid = models.ForeignKey(Entry, on_delete=models.CASCADE)
    time = models.DateTimeField()

class Status(models.Model):
    name = models.CharField(max_length=256, unique=True)

class StatusHistory(models.Model):
    uid = models.IntegerField(primary_key=True)
    entry_uid = models.ForeignKey(Entry, on_delete=models.CASCADE)
    time = models.DateTimeField()
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
