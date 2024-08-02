from django.db import models

class Student(models.Model):
    name= models.CharField(max_length=100)

    def __str__(self): 
        return self.name
    
class Course(models.Model):
    name= models.CharField(max_length=100)
    students=models.ManyToManyField('Student',related_name='courses')

    def __str__(self):
        return self.name  


# Create your models here.
