from django.db import models

# Create your models here.

class clientsTable(models.Model):
    name = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return '{}'.format(self.name)