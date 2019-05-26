from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.item_name, self.description)
