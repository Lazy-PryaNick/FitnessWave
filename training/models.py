from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    class Meta:
        ordering = ["price"]

    name = models.CharField(max_length=50, blank=True, null=True)
    price = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to="products")
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class ContactProfile(models.Model):
    class Meta:
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name",max_length=100)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return f'{self.name}'

class UserProfile(models.Model):
    class Meta:
        ordering = ["name"]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
