from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=12)
    description=models.TextField(default="Something")

    def __str__(self):
        return self.email
    
class Enrollment(models.Model):
    fullname=models.CharField(max_length=50)
    email=models.EmailField()
    gender=models.CharField(max_length=25)
    phonenumber=models.CharField(max_length=12)
    DOB=models.CharField(max_length=50)
    selectmembershipplan=models.CharField(max_length=12)
    selecttrainer=models.CharField(max_length=12)
    reference=models.CharField(max_length=12)
    address=models.TextField()
    paymentstatus=models.CharField(max_length=55, blank=True, null=True)
    price=models.IntegerField(max_length=55, blank=True, null=True)
    duedate=models.DateField(blank=True, null=True)
    timestamp=models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.email
    
class Trainer(models.Model):
    name=models.CharField(max_length=55)
    gender=models.CharField(max_length=25)
    phone=models.CharField(max_length=12)
    salary=models.IntegerField()
    def __str__(self):
        return self.name

class MembershipPlan(models.Model):
    plan=models.CharField(max_length=150)
    price=models.IntegerField()
    def __str__(self):
        return self.id