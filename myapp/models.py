from django.db import models

class gmodel(models.Model):
    title= models.CharField(max_length=200)
    des  = models.TextField()

    def __str__(self):
        return self.title

# Create your models here.
