from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Transport(models.Model):
    category = models.ForeignKey(to='Categories', on_delete=models.CASCADE)
    make = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    price = models.IntegerField()
    image = models.ImageField(upload_to='conf/', blank=True, null=True)


    def __str__(self):
        return f'{self.category.name} {self.model}'
