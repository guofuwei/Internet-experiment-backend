from django.db import models


class Device(models.Model):
    id = models.AutoField(primary_key=True)
    sn = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)
    is_speak = models.BooleanField(default=False)

    class Meta:
        db_table = 'device'
