from django.db import models

class Lokasi(models.Model):
    nama = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.nama