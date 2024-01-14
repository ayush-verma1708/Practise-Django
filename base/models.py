from django.db import models

# Create your models here.

class items(models.Model):
    name = models.CharField(max_length = 255)
    price = models.FloatField()

    def __str__(self):
        return self.name

class restaurant_menu(models.Model):
    items = models.ManyToManyField(items)

class restaurant(models.Model):
    R_id = models.IntegerField(null = False)
    R_name = models.CharField(null = False , max_length = 255)
    R_location = models.CharField(max_length = 255)
    restaurant_menu = models.OneToOneField(restaurant_menu , on_delete = models.CASCADE )

    def __str__(self):
        return self.R_name