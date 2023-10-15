from django.db import models

# Create your models here.

class State(models.Model):
    name = models.CharField(max_length = 50)
    image = models.ImageField(upload_to='')
    description = models.TextField(null=False)

    def __str__(self):
        return self.name
    

class Location(models.Model):
    name = models.CharField(max_length=50)
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='locations')
    description = models.TextField()

    def __str__(self):
        return self.name
