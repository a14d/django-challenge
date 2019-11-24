from django.db import models
import uuid

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=20)
    max_students = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering: ['name']

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name  = models.CharField(max_length=20)
    reference  = models.UUIDField(default=uuid.uuid4, editable=False)

    # relationships
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        ordering: ['first_name']