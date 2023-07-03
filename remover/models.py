from django.db import models
from datetime import datetime

# Create your models here.

class WaterMarkRemove(models.Model):
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True)
    sdate = models.DateTimeField(default=datetime.now)
    
    def __str__(self) -> str:
        return super().__str__()
