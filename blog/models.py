from django.db import models

# Create your models here.


class Post(models.Model):
  
    name = models.CharField(max_length=200)
    des = models.TextField()
    def __str__(self):
         return 'ชื่อรีวิว: ' + self.name
