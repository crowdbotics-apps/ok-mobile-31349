from django.conf import settings
from django.db import models


class School(models.Model):
    "Generated Model"
    levels = models.CharField(
        max_length=256,
    )
    teachers = models.CharField(
        max_length=256,
    )
