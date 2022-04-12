from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here
class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Branch(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Professor(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="professor")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department')
    email = models.EmailField(unique=True)
    contact_number = models.BigIntegerField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(models.Model):
    enroll_number = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='branch')
    email = models.EmailField(unique=True)
    contact_number = models.BigIntegerField(unique=True)
    qr_code = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.fullname

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"