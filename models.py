from django.db import models

class Competitor(models.Model):
    full_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=15, unique=True)
    national_id = models.CharField(max_length=50, unique=True)
    club_name = models.CharField(max_length=255)
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

