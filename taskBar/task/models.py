from django.db import models
from category.models import CategoryModel

# Create your models here.
class TaskModel(models.Model):
    id = models.IntegerField(primary_key=True, max_length=50)
    title = models.CharField(max_length=50)
    task_details = models.TextField()
    is_completed = models.BooleanField(default=False)
    category = models.ManyToManyField(CategoryModel)
    assign_date = models.DateField()
    def __str__(self):
        return f"{self.title} - {self.is_completed}"