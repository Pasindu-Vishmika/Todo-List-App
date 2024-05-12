from django.db import models
from django.contrib.auth.models import User , AbstractUser

class User (AbstractUser):
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =[]

class Task(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created'] 
        
    def __str__(self):
        return self.title
