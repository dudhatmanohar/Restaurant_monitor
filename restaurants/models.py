from django.db import models
class StoreStatus(models.Model):
    store_id = models.CharField(max_length=255)
    status = models.CharField(max_length=10)  # 'active' or 'inactive'
    timestamp_utc = models.DateTimeField()

class BusinessHours(models.Model):
    store_id = models.IntegerField()
    day_of_week = models.IntegerField()
    start_time_local = models.TimeField()
    end_time_local = models.TimeField()

class StoreTimezone(models.Model):
    store_id = models.IntegerField()
    timezone_str = models.CharField(max_length=50)

