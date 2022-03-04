from django.db import models


class Payment(models.Model):
    User_id = models.CharField(max_length=50, blank=True)
    UPI_id = models.CharField(max_length=50, blank=True)


    def __str__(self):
        return self.User_id
