from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here
class Professor(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    contact_number = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(models.Model):
    enroll_number = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    contact_number = models.IntegerField(unique=True)
    qr_code = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
