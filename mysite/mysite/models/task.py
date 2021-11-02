from django.db import models

class task(models.Model):
    id = models.CharField(unique=True,auto_created=True)
    title = models.CharField(required=True)
    description = models.CharField(required=True)
    status = models.CharField(max_length=11,choices=TYPE_SELECT)
    date = models.DateField(required=True)