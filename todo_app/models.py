from django.db import models

# Create your models here.
class Todo(models.Model):
    id = models.BigAutoField(primary_key=True),
    title = models.CharField(max_length=255, null=False),
    completed = models.BooleanField(default=False, blank=True, null=True)

    # def __str__(self):
    #     return self.title



