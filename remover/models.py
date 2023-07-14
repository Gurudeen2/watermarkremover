from django.db import models
from datetime import datetime

# Create your models here.

class WaterMarkRemove(models.Model):
    photo = models.ImageField(upload_to="photo/watermarked/%Y/%m/%d/", blank=True)
    sdate = models.DateTimeField(default=datetime.now)
    
    def __str__(self) -> str:
        return super().__str__()


class RemoveBackground(models.Model):
    photo = models.ImageField(upload_to="photo/removebg/%Y/%m/%d/", blank=True)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return self.date
