from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customers")
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)


    def __str__(self):
        return f"{self.user.name} - {self.city}"
    

    
