from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    created=models.DateTimeField()
    def __str__(self):
        return self.title
