from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.TextField()
    def __str__(self):
        return self.email
    
class Enrollment(models.Model):
    fullname=models.CharField(max_length=55)
    email=models.EmailField()
    gender=models.CharField(max_length=25)
    phonenumber=models.CharField(max_length=15)
    DOB=models.CharField(max_length=50)
    selectmembershipplan=models.CharField(max_length=55)
    selecttrainer=models.CharField(max_length=55)
    reference=models.CharField(max_length=55)
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
    phonenumber=models.CharField(max_length=15,default="Something")
    salary=models.IntegerField()
    def __str__(self):
        return self.name

class MembershipPlan(models.Model):
    plan=models.CharField(max_length=150)
    price=models.IntegerField()
    def __int__(self):
        return self.id
    
class Gallery(models.Model):
    title=models.CharField(max_length=100)
    img=models.ImageField(upload_to="Gallery")
    timestamp=models.DateTimeField(auto_now_add=True, blank=True)
    def __int__(self):
        return self.id
    
class Attendance(models.Model):
    selectdate=models.DateTimeField(auto_now_add=True)
    phonenumber=models.CharField(max_length=15)
    login=models.CharField(max_length=100)
    logout=models.CharField(max_length=100)
    selectworkout=models.CharField(max_length=100)
    trainedby=models.CharField(max_length=100)
    def __int__(self):
        return self.id
