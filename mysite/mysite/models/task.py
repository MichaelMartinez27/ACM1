from django.db import models

class task(models.Model):
    id = models.CharField("id",unique=True,auto_created=True)
    title = models.CharField("title")
    description = models.CharField("description")
    status = models.CharField(max_length=11,choices=TYPE_SELECT)
    date = models.DateField("date")