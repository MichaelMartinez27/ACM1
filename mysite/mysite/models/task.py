from django.db import models

class task(models.Model):
    id = models.CharField("id",unique=True,auto_created=True)
    title = models.CharField("title")
    description = models.CharField("description")
    status = models.BooleanField("status",default=False)
    date = models.DateField("date")