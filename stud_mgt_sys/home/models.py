from django.db import models

# Create your models here.
class Student(models.Model):  # Use PascalCase for class names
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField(unique=True)  # Added unique constraint for roll number
    marks = models.IntegerField()

    class Meta:
        db_table = 'add_student'  # Custom table name in the database

    def __str__(self):
        return f"{self.name} ({self.roll_no})"
