from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    # id = models.AutoField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name