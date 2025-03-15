from django.db import models

class emplo(models.Model):
    fname = models.CharField(max_length=255)
    image = models.ImageField(upload_to="uploads")
    
    def __str__(self):
        return self.fname
# Create your models here.
