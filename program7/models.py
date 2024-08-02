from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    student = models.ForeignKey(Student, related_name='projects', on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)
    languages = models.CharField(max_length=200)
    duration = models.IntegerField(help_text="Duration in days")  # You can use DurationField if you prefer

    def __str__(self):
        return f"{self.topic} by {self.student.name}"

# Create your models here.
